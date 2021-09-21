class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

sumarr = []

def printpaths(root):
    path = []
    printpathsrec(root, path, 0)

def printpathsrec(root, path, pathlen):
    
    if root is None:
        return
    
    if len(path) > pathlen:
        path[pathlen] = root.data
    else:
        path.append(root.data)
    
    pathlen += 1
    
    if root.left is None and root.right is None:
        sumarray(path, pathlen)
    else:
        printpathsrec(root.left, path, pathlen)
        printpathsrec(root.right, path, pathlen)

def sumarray(path, len):
    val = ''
    for i in path[0:len]:
        print(i, " ", end="")
    print()
    for i in path[0:len]:
        val += str(i)
    sumarr.append(val)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
# root.right.right = Node(7)

printpaths(root)

print(sumarr)

sum = 0
for i in sumarr:
        sum = sum + int(i)
print(sum)