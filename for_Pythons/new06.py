import sys
from timeit import repeat
x=int(input())
stdout=sys.stdout
Plist='Uno'
Tlist='Record'
Head='First'
Tail='Last'
Data=5

try:
    sys.stdout = open("C:\\Python3_11\\file01.py", 'r')
    a = sys.stdout.readlines()
    stdout.write("s")
finally:
    # Закрываем file
    sys.stdout.close()
    sys.stdout = stdout

while x!=None:
    x=int(input())
    x=x-1
    if x==0:

    elif x<0:

    
    else:
        x==None
        
        