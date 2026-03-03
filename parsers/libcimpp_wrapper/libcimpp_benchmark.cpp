#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <string>
#include <vector>
#include <memory>

#include "IEC61970.hpp"
#include "CIMModel.hpp"

namespace py = pybind11;

class LibCIMppBenchmark {
private:
    std::unique_ptr<CIMModel> model;

public:
    LibCIMppBenchmark() : model(std::make_unique<CIMModel>()) {}

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
};

PYBIND11_MODULE(_libcimpp_benchmark, m) {
    m.doc() = "libcimpp benchmark wrapper for Python";

    py::class_<LibCIMppBenchmark>(m, "LibCIMppBenchmark")
        .def(py::init<>())
        .def("load", &LibCIMppBenchmark::load,
             py::arg("file_paths"),
             "Load CIM files from the given paths")
        .def("count_acline_segments", &LibCIMppBenchmark::count_acline_segments,
             "Count ACLineSegment objects")
        .def("count_synchronous_machines", &LibCIMppBenchmark::count_synchronous_machines,
             "Count SynchronousMachine objects")
        .def("count_loads", &LibCIMppBenchmark::count_loads,
             "Count ConformLoad, NonConformLoad, and EnergyConsumer objects")
        .def("count_substations", &LibCIMppBenchmark::count_substations,
             "Count Substation objects");
}
