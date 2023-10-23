#include <Python.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        printf("[*] Invalid List Object\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;
    printf("[*] Allocated = %ld\n", allocated);

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        const char *item_type = Py_TYPE(item)->tp_name;
        
        printf("Element %ld: %s\n", i, item_type);
        
        if (PyBytes_Check(item)) {
            print_python_bytes(item);
        } else if (PyList_Check(item)) {
            print_python_list(item);
        } else if (PyFloat_Check(item)) {
            print_python_float(item);
        }
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        printf("[.] Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    
    const char *string = PyBytes_AsString(p);
    printf("  trying string: %s\n", string);
    
    printf("  first %d bytes: ", (size < 10) ? size : 10);
    for (Py_ssize_t i = 0; i < size && i < 10; i++) {
        printf("%02x ", (unsigned char)string[i]);
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        printf("[.] Invalid Float Object\n");
        return;
    }

    double value = PyFloat_AsDouble(p);
    printf("[.] float object info\n");
    printf("  value: %f\n", value);
}
PyMODINIT_FUNC PyInit_libPython(void) {
    return PyModule_Create(&libPythonModule);
}

