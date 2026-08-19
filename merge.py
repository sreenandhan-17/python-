def merge_sort(arr):
    # Base case: A list of 0 or 1 elements is already sorted
    if len(arr) <= 1:
        return arr

    # Step 1: Divide the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Step 2: Recursively sort both halves
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Step 3: Merge the two sorted halves
    return merge(sorted_left, sorted_right)


def merge(left, right):
    merged = []
    i = j = 0

    # Compare elements from left and right lists and append the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append any remaining elements from left or right lists
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


# Example usage
if __name__ == "__main__":
    sample_list = [38, 27, 43, 3, 9, 82, 10]
    print(f"Original list: {sample_list}")
    
    sorted_list = merge_sort(sample_list)
    print(f"Sorted list:   {sorted_list}")