class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

def preorder(root):
    if root:
        print(str(root.data) + "->", end=" ")
        preorder (root.left)
        preorder (root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.data) + "->", end=" ")
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.data) + "->", end=" ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Inorder Traversal:")
inorder(root)
print()

print("Preorder Traversal:")
preorder(root)
print()

print("Postorder Traversal:")
postorder(root)
print()