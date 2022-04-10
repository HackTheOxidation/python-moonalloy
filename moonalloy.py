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


# Initialize all functions in moonalloy
# array_print
_moonalloy.array_print.argtypes = [ctypes.POINTER(_Array_t)]
_moonalloy.array_print.restype = None

# array_ones
_moonalloy.array_ones.argtypes = [ctypes.c_int]
_moonalloy.array_ones.restype = ctypes.POINTER(_Array_t)

# array_zeros
_moonalloy.array_zeros.argtypes = [ctypes.c_int]
_moonalloy.array_zeros.restype = ctypes.POINTER(_Array_t)

# array_sum
_moonalloy.array_sum.argtypes = [ctypes.POINTER(_Array_t)]
_moonalloy.array_sum.restype = ctypes.c_double

# array_scalar
_moonalloy.array_scalar.argtypes = [ctypes.POINTER(_Array_t), ctypes.c_double]
_moonalloy.array_scalar.restype = ctypes.POINTER(_Array_t)

# Test
print("----- Initiating Test -----\n\n")

arr = _moonalloy.array_ones(ctypes.c_int(3))
print("Result: ")
_moonalloy.array_print(arr)
print()

arr2 = _moonalloy.array_zeros(ctypes.c_int(2))
print("Result: ")
_moonalloy.array_print(arr2)
print()

sum_result = _moonalloy.array_sum(arr)
print(f"Result: {sum_result}")
print()

scalar_result = _moonalloy.array_scalar(arr, ctypes.c_double(2.5))
print("Result: ")
_moonalloy.array_print(scalar_result)
print()
