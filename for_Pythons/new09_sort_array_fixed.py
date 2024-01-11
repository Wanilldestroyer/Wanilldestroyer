import package
ab=package.A()
ab.test()
with open('C:\\Python3_11\\inputt.py', 'r') as file:
    for line in file:
        cleaned_line = line.strip()
                
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Делим массив
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Рекурсивно сортируем
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Соединяем две части
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result
sorted_arr = merge_sort(cleaned_line)
print("Original array:", cleaned_line)
print("Sorted array:", sorted_arr)

with open('new_file.txt', 'x') as new_file:
    new_file.write('This is a new file.')