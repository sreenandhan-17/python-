def find_largest(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

# Example usage
arr = [3, 7, 2, 9, 4]
print("Largest:", find_largest(arr))
