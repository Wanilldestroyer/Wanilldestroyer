import sys
stdout=sys.stdout

tail = {"Tail":"hplkmnrASGSDFHcfghfgu\n","Mid":"hplkmnrASGSDFH\n","Head":"hplkmnrASGSDFHasd\n"}

head = {"Head":"hplkmnrASGSDFHasd\n","Mid":"hplkmnrASGSDFH\n","Tail":"hplkmnrASGSDFHcfghfgu\n"} 

def segment_1(head,file):
    if "Head" in head:
        if "Mid" in head:
            if "Tail" in head:
               file.write(head["Tail"])
               head.pop("Tail")
            else:
                print('no')
            file.write(head["Mid"])
            head.pop("Mid")
        else:
            print('no')
        file.write(head["Head"])
        head.pop("Head")
    else:    
        print('no')
        
def segment_2(tail,file):
    if "Tail" in tail:
        if "Mid" in tail:
            if "Head" in tail:
               file.write(tail["Head"])
               tail.pop("Head")
            else:
                print('no')
            file.write(tail["Mid"])
            tail.pop("Mid")
        else:
            print('no')
        file.write(tail["Tail"])
        tail.pop("Tail")
    else:    
        print('no')
# Открываем файл для чтения
file_path = "C:\\Python3_11\\file06_stack.txt"
with open(file_path, "w") as file:
    segment_1(head, file)
  

print(f"Values written to {file_path}")
print(head)

file_path = "C:\\Python3_11\\file006_stack.txt"
with open(file_path, "w") as file:
    segment_2(tail, file)

print(f"Values written to {file_path}")    
print(tail)