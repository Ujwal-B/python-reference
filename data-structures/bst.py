class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

def insert(node, item):
    if node == None:
        return Node(item)
    if item < node.data:
        node.left = insert(node.left, item)
    elif item > node.data:
        node.right = insert(node.right, item)
    return node

def inorderSuccessor(node):
    current = node
    while(node.left is not None):
        current = current.left
    return current

def deleteNode(root, item):
    if root is None:
        return root
    
    if item < root.data:
        root.left = deleteNode(root.left, item)
    elif item > root.data:
        root.right = deleteNode(root.right, item)
    
    #if the parent node has one child or no children
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp
        
        # if the parent node has 2 children
        # first find the inorder successor
        # then replace the inorder successor with the parent
        # delete the inorder successor from it's original place
        node = inorderSuccessor(root.right) # inorder successor is the smallest number larger than the parent number
        root.data = node.data

        # delete the old inorder successor node
        root.right = deleteNode(root.right, node.data)  # goes to the right subtree and starts searching for the data of inorder successor

    return root

def preorder(root):
    if root:
        print(str(root.data) + "->", end=" ")
        preorder(root.left)
        preorder(root.right)

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


root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)

inorder(root)        
print()

insert(root, 13)
inorder(root)        
print()

deleteNode(root, 13)
inorder(root)        
print()