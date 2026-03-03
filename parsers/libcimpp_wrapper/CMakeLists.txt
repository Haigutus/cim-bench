cmake_minimum_required(VERSION 3.12)
project(libcimpp_benchmark)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find Python
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)

# Find pybind11
find_package(pybind11 CONFIG REQUIRED)

# Find libcimpp (installed from .deb package)
# Headers are in /usr/include/cimpp/
# Library is in /usr/lib/

# Find all CGMES version directories
file(GLOB CGMES_VERSIONS "/usr/include/cimpp/CGMES_*")
list(LENGTH CGMES_VERSIONS CGMES_VERSION_COUNT)

if(CGMES_VERSION_COUNT EQUAL 0)
    message(FATAL_ERROR "No libcimpp CGMES version found in /usr/include/cimpp/")
endif()

# Use the first (and should be only) CGMES version found
list(GET CGMES_VERSIONS 0 CGMES_VERSION_DIR)
message(STATUS "Found CGMES version at: ${CGMES_VERSION_DIR}")

# Find the corresponding library
file(GLOB LIBCIMPP_LIBRARY "/usr/lib/libcimppCGMES*.so")
list(LENGTH LIBCIMPP_LIBRARY LIBCIMPP_COUNT)

if(LIBCIMPP_COUNT EQUAL 0)
    message(FATAL_ERROR "libcimpp library not found in /usr/lib/")
endif()

# Use the first library found
list(GET LIBCIMPP_LIBRARY 0 LIBCIMPP_LIBRARY)
message(STATUS "Found libcimpp library at: ${LIBCIMPP_LIBRARY}")

# Set include directories
set(LIBCIMPP_INCLUDE_DIRS "${CGMES_VERSION_DIR}" "/usr/include/cimpp/src" "/usr/include/cimpp/static" "/usr/include")

# Create pybind11 module
pybind11_add_module(_libcimpp_benchmark libcimpp_benchmark.cpp)

# Include directories
target_include_directories(_libcimpp_benchmark PRIVATE ${LIBCIMPP_INCLUDE_DIRS})

# Link against libcimpp
target_link_libraries(_libcimpp_benchmark PRIVATE ${LIBCIMPP_LIBRARY})

# Set RPATH to find libcimpp.so at runtime
set_target_properties(_libcimpp_benchmark PROPERTIES
    INSTALL_RPATH "/usr/lib"
    BUILD_WITH_INSTALL_RPATH TRUE
)
