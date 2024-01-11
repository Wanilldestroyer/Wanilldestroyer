import sys
stdout=sys.stdout

try:
    sys.stdout = open("C:\\Python3_11\\file03.py", 'r')
    a = sys.stdout.readlines()
        
finally:
    # Закрываем file
    sys.stdout.close()
    sys.stdout = stdout

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

# пример

arr = a
sorted_arr = merge_sort(a)
print("Original array:", arr)
print("Sorted array:", sorted_arr)
try:
    sys.stdout = open("C:\\Python3_11\\file001.py", 'w')
    print([10,15,20,34])
finally:
    # Закрываем file
    sys.stdout.close()
    sys.stdout = stdout
    