def sum_of_array(arr):
    total=0
    for num in arr:
        total += num
    return total

arr = [1, 2, 3, 4, 5]
result = sum_of_array(arr)
print(result)