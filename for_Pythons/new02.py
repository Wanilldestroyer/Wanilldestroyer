import sys
import random
stdout = sys.stdout
a=1
#sort answer in new09_sort_array file!
try:
    sys.stdout = open("C:\\Python3_11\\file01.py", 'r')
    a = sys.stdout.readlines()
        
finally:
    # Закрываем file
    sys.stdout.close()
    sys.stdout = stdout
print(a)
def cherry(a,b):
    if a == 0 or b ==0:
        return(a+a)
    else:
        return (a,b)
        

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

    elif responce ==3:
        on=random.randint(1,32)
        print(on)
    elif responce ==4:
        inputs.sort()
        print('sorted!')
    elif responce ==5:
        on=input("find the string")
        if on in inputs:
            print('Yes, it is!')
        else:
            print('No, its not!')

    else:
        print("Program is closed")
        break
    
    
x=cherry(17,0)
a.sort()
#if type(a)==list:
    

try:
    sys.stdout = open("C:\\Python3_11\\file01.py", 'w')
    print(10, sep='')
    print(15, sep='')
    print(20, sep='')
    print(x, sep='')
finally:
    # Закрываем file
    sys.stdout.close()
    sys.stdout = stdout
