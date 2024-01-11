"""JUST A COPY FROM OTHER FILE
#Wariant of generation defind (def) for recursion algoritm
import sys
stdout = sys.stdout
arrays = sys.argv[:]
def gen(x,y):
    for c in range(1,x+1):
        yield c+x
#try block
n=gen(5,2)
print(n.__next__())

    
FUCK FUCK FUCK
inputs = []
print("*","Your table with hash", "*")
responce=1
while responce:
    print("""choose:
          1-input string
          2-string from a file
          3-random string
          4-sort table
          5-find your string number""")
    responce = int(input("!>>"))
    if responce ==1:
        on = input("input new string to array")
        inputs.append(on)
    elif responce ==2:
        l=str(input("Type your promt"))
#code for OPENING file from path you solve (l)
try:
    sys.stdout = open("C:\\Python3_11\\file01.py", 'r')
    a = sys.stdout.readlines()
finally:
    pass
    elif responce ==3:
        on=random.randint(1,32)
        print(on)
    elif responce ==3:
        inputs.sort()
        print('sorted!')
    elif responce ==3:
        on=input("find the string")
        if on in inputs:
            print('Yes, it is!')
        else:
            print('No, its not!')

    else:
        print("Program is closed")
        break
    

        """

"""
len("123456")
    
if "111\n" in a:
    for b in sorted(a):
        print('1')

        rand=random.randint(1,32)
        b+="string"
        
        
else:
    for b in range(len("123456")):
    
if len(a)<4:
    #do stuff
    for b in range(len("123456")):
        print(s[:-1:])
        s=s[1:-1:2]
        if "1000" in a:
            break
        
for n in arrays:
    print(n)
    
else:
    for b in range(1,n):
        simple coding
        break


try:
    sys.stdout = open("C:\\Python3_11\\file01.py", 'r')
    a = sys.stdout.readlines()
finally:
    # Закрываем file
    sys.stdout.close()
    sys.stdout = stdout

    
try:
    sys.stdout = open("C:\\Python3_11\\file01.py", 'w')
    print('Bebra cadebraaa')
    print('12')
    print('111')
finally:
    # Закрываем file
    sys.stdout.close()
    sys.stdout = stdout
    

"""




#import numpy as np
"""
import sys
import random
import math
stdout = sys.stdout
a=1
b=[]
p=str
x=int
h=str
this_file=''
text='9'

try:
    sys.stdout = open("C:\\Python3_11\\file03.py", 'r')
    a = sys.stdout.readlines()
    

finally:
    # Закрываем file
    sys.stdout.close()
    sys.stdout = stdout
# перечисляем список    

if x is not list:
    for b in range(len(a)):
        
    
# question?
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

# Example usage
ordered_array = [1, 3, 5, 7, 9, 11, 13, 15]
target_number = 8

position = find_position(ordered_array, target_number)

print(f"The position for {target_number} is {position}")

if a.count(c) is True:

#for min maxing list on python!
x=min(a)

x=max(a)

#sort method for python(its sorting list!)
a.sort(reverse=False)
#for convert to string!!
h="".join(a)
for numpy )
grid=np.a(shape(10,10), dtype=float)   
#index method for list!!!!
if a.index(c) is True:
    x=a.index(c)
    
    
else:
    code



FOR LAB_8 theme 
x_list = list(range(0,5))
y1_list = [22,17,81,41,25]
plt.plot(x_list, y1_list)
plt.show()

FOR SCANNING DOCUMENT WITHOUT SYS
with open('your_file.txt', 'r') as file:
    line = file.readline().strip()

print(line)

Version with FOR cycle:
with open('your_file.txt', 'r') as file:
    for line in file:
        cleaned_line = line.strip()
        print(cleaned_line)
        
FOR LIST_STACK_LR_6


import sys
stdout=sys.stdout
p=int(10)

def Node2(First,Last):
    First={}
    First["Head"]=1
    First["None"]=None
    Last={}
    Last["Tail"]=None
    Mid=First["None"]
    for First in range(1,p+1):
        First["Tail"]=3
        yield p+First
    return Mid
d=Node2(3,3)
print(d.__next__())
print(d.__next__())
print(d.__next__())


try:
    sys.stdout = open("C:\\Python3_11\\file06_stack.txt", 'w')

finally:
    # Закрываем file
    sys.stdout.close()
    sys.stdout = stdout
    
FOR LAB_4_hash_function_B

import random
stdout = sys.stdout
data=1




class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, data):
        # Convert the input string to a sequence of 32-bit blocks
        block=int()
        blocks = [data[i:i+32] for i in range(0, len(data), 32)]

        # Calculate the hash value by summing up the 32-bit blocks and discarding overflow
        hash_value = sum(int(block, 2) for block in blocks) % self.size

        return hash_value

    def insert(self, data):
        hash_value = self.hash_function(data)

        # Insert the data and its hash value into the hash table
        if self.table[hash_value] is None:
            self.table[hash_value] = [(data, hash_value)]
        else:
            self.table[hash_value].append((data, hash_value))

    def search(self, query):
        hash_value = self.hash_function(query)

        # Search for the query in the hash table
        if self.table[hash_value] is not None:
            for data, value in self.table[hash_value]:
                if data == query:
                    return f"String '{query}' found with hash value {value}."

        return f"String '{query}' not found."

# Example usage

hash_table_size = 100
hash_table = HashTable(hash_table_size)


# Input data
file_data = "10100111010111001001010001111111100100011001010000010000000110100000010001001010001111110000100011000110100101111110"

# Insert data into the hash table
hash_table.insert(file_data)

# Search for a string entered from the keyboard
search_query = input("Enter a string to search: ")
result = hash_table.search(search_query)
print(result)
"""