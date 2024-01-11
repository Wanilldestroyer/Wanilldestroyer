import sys
stdout=sys.stdout

tail = {"Head":"None","Mid":"String that i input","Tail":None}
segment3 = {"Head":"None","Mid":"String that i input","Tail":"Mid"}
segment2 = {"Head":"None","Mid":"String that i input","Tail":"Mid"}
segment1 = {"Head":"None","Mid":"String that i input","Tail":"Mid"}
head = {"Head":"None","Mid":"String that i input","Tail":"Mid"}
class Head:
    def __init__(self, data=p, next_node=head):
        self.data = data
        self.next_node = next_node

def write_list_to_file(head, file):
    if head != 10:
        n = head
        file.write(n)
        head=1
        head+=1
        Node(head,file)



class segment:
    def __init__(self, segment=str, next_node=str):
        self.segment=segment
        self.next_node=next_node
        
def segment_1(head,file):
    if head.pop("Head") is "None":
        file.write("hplkmnrASGSDFH")
        Node(head,file)


# Создаем связанный список



#из программы-словаря
# Открываем файл для чтения
file_path = "C:\\Python3_11\\file06_stack.txt"
with open(file_path, "w") as file:
    write_list_to_file(head, file)

print(f"Values written to {file_path}")


