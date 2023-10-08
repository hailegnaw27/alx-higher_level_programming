#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints basic info about Python lists
 * @p: pointer to PyObject
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *obj;

    size = PyList_Size(p);
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        obj = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(obj)->tp_name);
    }
}
