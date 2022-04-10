import moonalloy as ma

arr = ma.Array([1, 2, 3])
print(arr)

sum_result = arr.sum()
print(sum_result)

arr2 = ma.Array([2, 3, 5])
print(arr2)

add_result = arr + arr2
print(add_result)
