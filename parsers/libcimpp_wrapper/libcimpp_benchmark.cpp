#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <string>
#include <vector>
#include <memory>

#include "IEC61970.hpp"
#include "CIMModel.hpp"
#include "CIMWriter.hpp"
#include "CGMESProfile.hpp"
#include "CimConstants.hpp"
#include "version.hpp"

namespace py = pybind11;

class LibCIMppBenchmark {
private:
    std::unique_ptr<CIMModel> model;

public:
    LibCIMppBenchmark() : model(std::make_unique<CIMModel>()) {}

    static const std::string& get_release_version() {
        static const std::string release_version(RELEASE_VERSION);
        return release_version;
    }

    static const std::string& get_cim_version() {
        static const std::string cim_version(CimVersion);
        return cim_version;
    }

    bool load(const std::vector<std::string>& file_paths) {
        try {
            // Disable dependency checking for parsing
            model->setDependencyCheckOff();

            for (const auto& path : file_paths) {
                if (!model->addCIMFile(path)) {
                    py::print("Warning: File not found or not XML:", path);
                }
            }
            model->parseFiles();
            return true;
        } catch (const std::exception& e) {
            py::print("Error loading CIM files:", e.what());
            return false;
        }
    }

    size_t count_acline_segments() {
        size_t count = 0;
        for (BaseClass* obj : model->Objects) {
            if (dynamic_cast<CIMPP::ACLineSegment*>(obj)) {
                count++;
            }
        }
        return count;
    }

    size_t count_synchronous_machines() {
        size_t count = 0;
        for (BaseClass* obj : model->Objects) {
            if (dynamic_cast<CIMPP::SynchronousMachine*>(obj)) {
                count++;
            }
        }
        return count;
    }

    size_t count_loads() {
        size_t count = 0;
        for (BaseClass* obj : model->Objects) {
            if (dynamic_cast<CIMPP::ConformLoad*>(obj) ||
                dynamic_cast<CIMPP::NonConformLoad*>(obj) ||
                dynamic_cast<CIMPP::EnergyConsumer*>(obj)) {
                count++;
            }
        }
        return count;
    }

    size_t count_substations() {
        size_t count = 0;
        for (BaseClass* obj : model->Objects) {
            if (dynamic_cast<CIMPP::Substation*>(obj)) {
                count++;
            }
        }
        return count;
    }

    std::map<std::string, std::string> write(const std::string& output_path) {
        auto classProfileMap = CIMWriter::getClassProfileMap(model->Objects);
        std::map<CGMESProfile, std::string> profileFileMap = CIMWriter::writeFiles(output_path, model->Objects, output_path, classProfileMap);
        std::map<std::string, std::string> resultMap;
        for (const auto& profileAndFile : profileFileMap) {
            resultMap.emplace(getProfileShortName(profileAndFile.first), profileAndFile.second);
        }
        return resultMap;
    }
};

PYBIND11_MODULE(_libcimpp_benchmark, m) {
    m.doc() = "libcimpp benchmark wrapper for Python";

    py::class_<LibCIMppBenchmark>(m, "LibCIMppBenchmark")
        .def(py::init<>())
        .def("load", &LibCIMppBenchmark::load,
             py::arg("file_paths"),
             "Load CIM files from the given paths")
        .def_static("get_release_version", &LibCIMppBenchmark::get_release_version,
             "Get Release Version")
        .def_static("get_cim_version", &LibCIMppBenchmark::get_cim_version,
             "Get CIM Version")
        .def("count_acline_segments", &LibCIMppBenchmark::count_acline_segments,
             "Count ACLineSegment objects")
        .def("count_synchronous_machines", &LibCIMppBenchmark::count_synchronous_machines,
             "Count SynchronousMachine objects")
        .def("count_loads", &LibCIMppBenchmark::count_loads,
             "Count ConformLoad, NonConformLoad, and EnergyConsumer objects")
        .def("count_substations", &LibCIMppBenchmark::count_substations,
             "Count Substation objects")
        .def("write", &LibCIMppBenchmark::write,
             py::arg("output_path"),
             "Write the CIM data to RDF/XML files separated by profiles. Returns written files as mapping of profile to file");
}
