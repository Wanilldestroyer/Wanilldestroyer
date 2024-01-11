import sys


#простая хаш функция:
def simple_hash_function(input_string):
    return hash(input_string)

# пример функции
my_string = str(input("Draw your promt"))
hash_value = simple_hash_function(my_string)

print(f"The hash value for '{my_string}' is: {hash_value}")


