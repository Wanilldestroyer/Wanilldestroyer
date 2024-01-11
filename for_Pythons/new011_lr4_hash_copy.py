import sys
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
    

#for simple hash function:
def simple_hash_function(input_string):
    return hash(input_string)

# Example usage
my_string = str(input("Draw your string"))
hash_value = simple_hash_function(my_string)

print(f"The hash value for '{my_string}' is: {hash_value}")


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