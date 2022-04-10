"""
Array wrappers for moonalloy
"""

import ctypes
from ffi import moonalloy_ffi as ffi


class _Array_t(ctypes.Structure):
    """
    Internal class for representing an Array from moonalloy in python.
    """
    _fields_ = [('len', ctypes.c_size_t),
                ('arr', ctypes.POINTER(ctypes.c_double))]


# Initialize all functions in moonalloy
# array_print
ffi.array_print.argtypes = [ctypes.POINTER(_Array_t)]
ffi.array_print.restype = None
array_print = ffi.array_print

# array_ones
ffi.array_ones.argtypes = [ctypes.c_int]
ffi.array_ones.restype = ctypes.POINTER(_Array_t)
array_ones = ffi.array_ones

# array_zeros
ffi.array_zeros.argtypes = [ctypes.c_int]
ffi.array_zeros.restype = ctypes.POINTER(_Array_t)
array_zeros = ffi.array_zeros

# array_sum
ffi.array_sum.argtypes = [ctypes.POINTER(_Array_t)]
ffi.array_sum.restype = ctypes.c_double
array_sum = ffi.array_sum

# array_scalar
ffi.array_scalar.argtypes = [ctypes.POINTER(_Array_t), ctypes.c_double]
ffi.array_scalar.restype = ctypes.POINTER(_Array_t)
array_scalar = ffi.array_scalar

# array_add
ffi.array_add.argtypes = [ctypes.POINTER(_Array_t),
                                 ctypes.POINTER(_Array_t)]
ffi.array_add.restype = ctypes.POINTER(_Array_t)
array_add = ffi.array_add

# array_sub
ffi.array_sub.argtypes = [ctypes.POINTER(_Array_t),
                                 ctypes.POINTER(_Array_t)]
ffi.array_sub.restype = ctypes.POINTER(_Array_t)
array_sub = ffi.array_sub

# array_mult
ffi.array_mult.argtypes = [ctypes.POINTER(_Array_t),
                                  ctypes.POINTER(_Array_t)]
ffi.array_mult.restype = ctypes.POINTER(_Array_t)
array_mult = ffi.array_mult

# array_dotp
ffi.array_dotp.argtypes = [ctypes.POINTER(_Array_t),
                                  ctypes.POINTER(_Array_t)]
ffi.array_dotp.restype = ctypes.c_double
array_dotp = ffi.array_dotp

# array_concat
ffi.array_concat.argtypes = [ctypes.POINTER(_Array_t),
                                    ctypes.POINTER(_Array_t)]
ffi.array_concat.restype = ctypes.POINTER(_Array_t)
array_concat = ffi.array_concat

# array_to_string
ffi.array_to_string.argtypes = [ctypes.POINTER(_Array_t)]
ffi.array_to_string.restype = ctypes.c_char_p
array_to_string = ffi.array_to_string


class ArithmeticError(BaseException):
    """
    Exception for arithmetic errors.
    """


class Array:
    """
    Wrapper class for arrays in moonalloy
    """
    _array_ptr: _Array_t
    _len: int

    def __init__(self, py_list=None):
        if py_list is not None:
            self._init_array_pointer(py_list)
            self._len = len(py_list)

    def _init_array_pointer(self, py_list):
        self._array_ptr = _Array_t()
        self._array_ptr.len = ctypes.c_size_t(len(py_list))

        internal_array = (ctypes.c_double * len(py_list))(*range(len(py_list)))

        for i, elem in enumerate(py_list):
            internal_array[i] = elem

        self._array_ptr.arr = internal_array

    def add(self, other):
        """
        Performs addition on this and another array.
        """
        if self._len != other._len:
            raise ArithmeticError("Moonalloy - Error: trying to add arrays with different lengths - operation is undefined.")
        new_arr = array_add(self._array_ptr, other._array_ptr)

        result = Array()
        result._array_ptr = new_arr
        result._len = self._len

        return result

    def __str__(self):
        return ""
