class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def search_in_tree(root, target):
    if not root:
        return False
    
    if root.value == target:
        return True

    # Рекурсивно обыскиваем правую и левую части
    left_search = search_in_tree(root.left, target)
    right_search = search_in_tree(root.right, target)

    return left_search or right_search

def compare_leftmost_rightmost(root):
    if not root:
        return False

    leftmost = find_leftmost(root)
    rightmost = find_rightmost(root)

    return leftmost.value == rightmost.value

def find_leftmost(root):
    if not root.left:
        return root
    return find_leftmost(root.left)

def find_rightmost(root):
    if not root.right:
        return root
    return find_rightmost(root.right)

# Пример
# Создаем бинарное дерево
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(18)

# Ищем элемент дерева
print('Type your number')
target_element = int(input())
result_search = search_in_tree(root, target_element)
print(f"Is {target_element} present in the tree? {result_search}")

# Сравниваем самый левый и самый правый листочки
result_compare = compare_leftmost_rightmost(root)
print(f"Are the leftmost and rightmost elements the same? {result_compare}")