import sys
stdout = sys.stdout
a=1
try:
    sys.stdout = open("C:\\Python3_11\\file01.py", 'r')
    a = sys.stdout.readlines()
    stdout.write("strin")
finally:
    # Закрываем file.txt
    sys.stdout.close()
    sys.stdout = stdout
print(a)
try:
    sys.stdout = open("C:\\Python3_11\\file01.py", 'w')
    print('Abra CADABRAAAAAAA')
finally:
    # Закрываем file.txt
    sys.stdout.close()
    sys.stdout = stdout