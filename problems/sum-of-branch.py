class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

num = []
sum = 0
arr = []

def branch_value(root):
    val = ''
    if root is None:
        # num.pop(-1)
        for i in num:
            val += str(i)
        arr.append(val)
        return
    print(root.data)
    num.append(root.data)
    branch_value(root.left)
    branch_value(root.right)
    print(num)
    num.pop()
    print(num)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

branch_value(root)

print(arr)

num = [v for i, v in enumerate(arr) if i%2 == 0]
for i in num:
    sum += int(i)
print(sum)
# print(root.data)
# print(root.left.data)
# print(root.right.data)