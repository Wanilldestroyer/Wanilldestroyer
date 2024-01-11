import heapq
import tempfile
import shutil
import os

def external_sort(input_filename, output_filename, block_size=1000):
# Step 1: Divide the file into sorted blocks
with open(input_filename, 'r') as input_file:
temp_files = []
temp_file_number = 0

while True:
block = input_file.readlines(block_size)
if not block:
break

block.sort()

temp_filename = f'temp_{temp_file_number}.txt'
temp_file_number += 1

with open(temp_filename, 'w') as temp_file:
temp_file.writelines(block)

temp_files.append(temp_filename)

# Step 2: Merge sorted blocks
with open(output_filename, 'w') as output_file:
with tempfile.TemporaryDirectory() as temp_dir:
temp_files_heap = [(open(temp_file), temp_file) for temp_file in temp_files]
heapq.heapify(temp_files_heap)

while temp_files_heap:
smallest_file, smallest_filename = heapq.heappop(temp_files_heap)
smallest_line = smallest_file.readline()

if smallest_line:
heapq.heappush(temp_files_heap, (smallest_file, smallest_filename))
else:
smallest_file.close()
os.remove(smallest_filename)

output_file.write(smallest_line)

# Cleanup temporary files
for temp_file in temp_files:
os.remove(temp_file)

# Пример использования
input_file = 'unsorted_data.txt'
output_file = 'sorted_data.txt'

# Запись неотсортированных данных в файл
with open(input_file, 'w') as f:
f.write("5\n3\n8\n1\n7\n2\n")

# Вызов функции внешней сортировки
external_sort(input_file, output_file)

# Вывод отсортированных данных
with open(output_file, 'r') as f:
print(f.read())