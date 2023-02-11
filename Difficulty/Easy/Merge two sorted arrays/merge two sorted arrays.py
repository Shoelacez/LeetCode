class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    list1 = []
    list2 = []

    def __init__(self):
        self.head = None

    def printList(self):
        h = self.head
        if h is None:
            print("LL is empty")

        else:
            while h is not None:
                print(f"{h.data}->", end="")
                self.list1.append(h.data)
                h = h.ref

    def insert(self, num):
        # create a node
        new_node = Node(num)
        # connect the new_node  to the head
        new_node.ref = self.head
        # set the new_node as the head
        self.head = new_node

    def merge(self, l1, l2):
        pass

    def createL1(self):
        selection = "#"
        while not selection:
            input("Num: ")


ll = LinkedList()
# ll.insert(3)
# ll.insert(2)
# ll.insert(1)
ll.createL1()

ll.printList()