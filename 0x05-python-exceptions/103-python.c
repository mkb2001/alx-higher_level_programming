
#include <Python.h>
#include <stdio.h>
#include "cpython.h"
/**
 * print_python_list - Prints basic information about a Python list
 * @p: Pointer to a PyObject representing the list
 */
void print_python_list(PyObject *p)
{
    PyListObject *list;
    Py_ssize_t size, allocated, i;
    PyObject *item;

    if (!PyList_Check(p))
    {
        printf("[ERROR] Invalid List Object\n");
        return;
    }

    list = (PyListObject *)p;
    size = PyList_GET_SIZE(p);
    allocated = list->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GET_ITEM(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
        if (PyBytes_Check(item))
            print_python_bytes(item);
        else if (PyFloat_Check(item))
            print_python_float(item);
    }
}

/**
 * print_python_bytes - Prints basic information about a Python bytes object
 * @p: Pointer to a PyObject representing the bytes object
 */
void print_python_bytes(PyObject *p)
{
    /** PyBytesObject *bytes;**/
    Py_ssize_t size, i;
    char *str;

    if (!PyBytes_Check(p))
    {
        printf("[ERROR] Invalid Bytes Object\n");
        return;
    }

    /** bytes = (PyBytesObject *)p;**/
    size = PyBytes_GET_SIZE(p);
    str = PyBytes_AS_STRING(p);

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);
    printf("  first %ld bytes: ", (size < 10) ? size + 1 : 10);

    for (i = 0; i < ((size < 10) ? size : 10); i++)
        printf("%02x ", (unsigned char)str[i]);

    printf("\n");
}

/**
 * print_python_float - Prints basic information about a Python float object
 * @p: Pointer to a PyObject representing the float object
 */
void print_python_float(PyObject *p)
{
    PyFloatObject *float_obj;
    double value;

    if (!PyFloat_Check(p))
    {
        printf("[ERROR] Invalid Float Object\n");
        return;
    }

    float_obj = (PyFloatObject *)p;
    value = float_obj->ob_fval;

    printf("[.] float object info\n");
    printf("  value: %g\n", value);
}