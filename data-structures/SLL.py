class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def bsort(self):
        cur = self.head
        while(cur != None):
            index = cur.next
            while (index != None):
                if (index.item < cur.item):
                    temp = cur.item
                    cur.item = index.item
                    index.item = temp
                index = index.next
            cur = cur.next

    def search(self, item):
        cur = self.head
        count = 0
        while(cur != None):
            count += 1
            if (cur.item == item):
                return count
            cur = cur.next
        if cur == None:
            return False
    
    def deleteNode(self, item):
        if self.head == None:
            return
        cur = self.head
        pre = self.head
        while(cur.next != None):
            if (cur.item == item):
                temp = cur
                cur = cur.next
                temp = None
            pre = cur
            cur = cur.next
    
    def binsert(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def minsert(self, item, pos):
        new_node = Node(item)
        cur = self.head
        pre = self.head
        count = 0
        while(cur != None):
            if count != pos:
                count += 1
            else:
                pre.next = new_node
                new_node.next = cur
                break
            pre = cur
            cur = cur.next

    def einsert(self, item):
        new_node = Node(item)
        cur = self.head
        pre = self.head
        while cur != None:
            pre = cur
            cur = cur.next
        pre.next = new_node
    
    def listPrint(self):
        ptr = sll.head
        while (ptr != None):
            print(ptr.item, end="  ")
            ptr = ptr.next
        print()




sll = LinkedList()

sll.head = Node(3)
second = Node(2)
third = Node(1)
fourth = Node (4)

sll.head.next = second
second.next = third
third.next = fourth

ptr = sll.head
sll.listPrint()

print(sll.search(3))

sll.binsert(9)
sll.listPrint()

sll.minsert(13,2)
ptr = sll.head
sll.listPrint()

sll.einsert(15)
ptr = sll.head
sll.listPrint()

sll.bsort()
ptr = sll.head
sll.listPrint()

sll.deleteNode(1)
ptr = sll.head
sll.listPrint()