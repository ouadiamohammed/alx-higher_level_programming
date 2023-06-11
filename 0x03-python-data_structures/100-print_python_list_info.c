#include <object.h>
#include <Python.h>
#include <listobject.h>

/**
 * print_python_list_info - prints info about python lists
 * @p: python object
*/

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	PyObject *obj;

	size = Pylist_Size(p);
	alloc = ((PylistObject *)p)->allocated;
	i = 0;

	printf("[*] size of the python List = %li\n", size);
	printf("[*] allocated = %li\n", obj->allocated);

	while (i < size)
	{
		print("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i]->tp_name));
		i++;
	}
}
