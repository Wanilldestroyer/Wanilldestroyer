def find_position(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Found the target
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    # If the target is not in the array, low represents the position to insert the target
    return low

ordered_array = [1, 3, 5, 7, 9, 11, 13, 15]
target_number = 12

position = find_position(ordered_array, target_number)

print(f"The position for {target_number} is {position}")