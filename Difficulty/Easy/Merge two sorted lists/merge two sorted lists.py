l1 = [1, 2, 4]
l2 = [1, 3, 4]


class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, num):
        # 1. Create the Node to be inserted
        new_node = Node(num)
        # 2. the new_node inserted at the beginning
        new_node.ref = self.head
        # Assigning the new node to the head
        self.head = new_node

    def traverse_ll(self):
        if self.head == None:
            print("List is empty")
        else:
            h = self.head

            while h:
                print(f"{h.data}")
                h = h.ref

ll = LinkedList()
ll.insert(11)
ll.insert(23)
ll.insert(22)
ll.traverse_ll()