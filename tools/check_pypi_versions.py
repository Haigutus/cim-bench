#!/usr/bin/env python3
"""Check PyPI for latest versions of tool dependencies."""

import json
import re
import sys
import tomllib
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError


def get_pypi_latest_version(package_name):
    """Get latest version of a package from PyPI."""
    # Normalize package name (PyPI is case-insensitive, uses dashes)
    normalized_name = package_name.lower().replace("_", "-")
    url = f"https://pypi.org/pypi/{normalized_name}/json"

    try:
        req = Request(url, headers={'User-Agent': 'cim-bench-version-checker'})
        with urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
            return data['info']['version']
    except URLError as e:
        return f"Error: {e}"
    except KeyError:
        return "Error: Invalid response"
    except Exception as e:
        return f"Error: {e}"


def parse_dependency_spec(dep_spec):
    """Parse dependency specification like 'package>=1.0.0' into (package, operator, version)."""
    # Match patterns like: package>=1.0.0, package==1.0.*, package>1.0
    match = re.match(r'([a-zA-Z0-9_-]+)\s*(>=|==|>|<|<=|~=)?\s*(.+)?', dep_spec)
    if match:
        package = match.group(1)
        operator = match.group(2) or ""
        version = match.group(3) or ""
        return package, operator, version
    return dep_spec, "", ""


def load_tool_dependencies(tool_config_path):
    """Load dependencies from a tool's pyproject.toml."""
    with open(tool_config_path, 'rb') as f:
        config = tomllib.load(f)

    python_version = config.get('project', {}).get('requires-python', 'Not specified')
    dependencies = config.get('project', {}).get('dependencies', [])

    return python_version, dependencies


def load_common_dependencies():
    """Load common testing framework dependencies."""
    common_path = Path('tool-configs/common/requirements.txt')
    if not common_path.exists():
        return []

    with open(common_path) as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]


def discover_tools_from_compose():
    """Extract unique tool names from docker-compose.yml by parsing image names."""
    import subprocess

    try:
        # Use podman-compose to get the config
        result = subprocess.run(
            ['podman-compose', '-f', 'docker/docker-compose.yml', 'config'],
            capture_output=True,
            text=True,
            check=True
        )

        # Extract image names that start with cim-bench/ (excluding base)
        tools = set()
        for line in result.stdout.splitlines():
            if 'image:' in line:
                # Extract image name like "cim-bench/triplets:latest"
                match = re.search(r'cim-bench/([a-z]+):', line)
                if match and match.group(1) != 'base':
                    tools.add(match.group(1))

        return sorted(tools)

    except subprocess.CalledProcessError as e:
        print(f"Error running podman-compose: {e}", file=sys.stderr)
        return []
    except FileNotFoundError:
        print("Error: podman-compose not found", file=sys.stderr)
        return []


def compare_versions(current, latest):
    """Simple version comparison to highlight if update available."""
    if current.startswith('==') or current.startswith('>='):
        current_clean = current[2:].strip()
    else:
        current_clean = current.strip()

    # Handle wildcards like 3.14.*
    if '*' in current_clean:
        current_clean = current_clean.replace('.*', '')

    if latest.startswith('Error:'):
        return '❌'

    # Simple string comparison (not semver-aware, but good enough for display)
    if current_clean == latest:
        return '✓'
    elif current_clean < latest:
        return '⬆️'
    else:
        return '?'


def main():
    print("=" * 80)
    print("cim-bench Dependency Version Check (PyPI)")
    print("=" * 80)
    print()

    # Discover tools from docker-compose.yml
    print("📦 Discovering tools from docker-compose.yml...")
    tools = discover_tools_from_compose()

    if not tools:
        print("❌ No tools found. Make sure docker/docker-compose.yml exists.")
        return 1

    print(f"   Found {len(tools)} tools: {', '.join(tools)}")
    print()

    # Check common dependencies
    print("=" * 80)
    print("Common Testing Framework Dependencies")
    print("=" * 80)

    common_deps = load_common_dependencies()
    if common_deps:
        print(f"{'Package':<25} {'Current':<15} {'Latest':<15} {'Status':<8}")
        print("-" * 80)

        for dep_spec in common_deps:
            package, operator, version = parse_dependency_spec(dep_spec)
            latest = get_pypi_latest_version(package)
            status = compare_versions(f"{operator}{version}", latest)

            current_display = f"{operator}{version}" if version else "any"
            print(f"{package:<25} {current_display:<15} {latest:<15} {status:<8}")
    else:
        print("   No common dependencies found")

    print()

    # Check each tool's dependencies
    for tool in tools:
        config_path = Path(f'tool-configs/{tool}/pyproject.toml')

        if not config_path.exists():
            print(f"⚠️  {tool}: Config not found at {config_path}")
            print()
            continue

        print("=" * 80)
        print(f"{tool.upper()} Dependencies")
        print("=" * 80)

        python_version, dependencies = load_tool_dependencies(config_path)
        print(f"Python: {python_version}")
        print()

        if not dependencies:
            print("   No tool-specific dependencies")
            print()
            continue

        print(f"{'Package':<25} {'Current':<15} {'Latest':<15} {'Status':<8}")
        print("-" * 80)

        for dep_spec in dependencies:
            package, operator, version = parse_dependency_spec(dep_spec)
            latest = get_pypi_latest_version(package)
            status = compare_versions(f"{operator}{version}", latest)

            current_display = f"{operator}{version}" if version else "any"
            print(f"{package:<25} {current_display:<15} {latest:<15} {status:<8}")

        print()

    print("=" * 80)
    print("Legend:")
    print("  ✓  = Using latest version")
    print("  ⬆️  = Update available")
    print("  ❌ = Error checking PyPI")
    print("  ?  = Version comparison unclear")
    print("=" * 80)

    return 0


if __name__ == "__main__":
    sys.exit(main())
