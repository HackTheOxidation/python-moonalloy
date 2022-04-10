"""
Test moonalloy in python
"""
import ctypes

# Load moonalloy
_moonalloy = ctypes.CDLL("./moonalloy/target/debug/libmoonalloy.so")


class _Array_t(ctypes.Structure):
    """
    Internal class for representing an Array from moonalloy in python.
    """
    array_new = _moonalloy

    _fields_ = [('len', ctypes.c_size_t),
                ('arr', ctypes.POINTER(ctypes.c_double))]


# initialize all functions in moonalloy
_moonalloy.array_print.argtypes = [ctypes.POINTER(_Array_t)]
_moonalloy.array_print.restype = None

_moonalloy.array_ones.argtypes = [ctypes.c_int]
_moonalloy.array_ones.restype = ctypes.POINTER(_Array_t)


arr = _moonalloy.array_ones(ctypes.c_int(3))
print("Result: ")
_moonalloy.array_print(arr)
