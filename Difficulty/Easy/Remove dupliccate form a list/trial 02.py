class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, num):
        new_node = Node(num)
        cur = self.head

        while cur.next != None:
            cur = cur.next

        cur.next = new_node

    def printList(self):
        pass


print(LinkedList.append(1))