# Revision on singly linked lists
# 1. Create the Node
# A node comprises the fields data and link
# Node class creates individual nodes, that is they are not linked
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


# 2. Linking the individual nodes
class LinkedList:
    def __init__(self):
        self.head = None

    # Adding methods to perform some operations
    # 1. Insertion
    # 2. Deletion
    # 3. traversal
    def insertion_beginning(self, num):
        # 1. Create the node to be inserted at the beginning
        new_node = Node(num)
        # 2. change the link of the new node to point to the previous first node
        new_node.ref = self.head
        # 3. Assigning new_node to be the head
        self.head = new_node

    def insertion_end(self):
        pass

    def insertion_between_nodes(self):
        pass

    def deletion(self):
        pass

    def traversal(self):
        n = self.head
        if n is None:
            print(f"Singly linked list is empty")
        else:
            while n:
                print(n.data)
                n = n.ref


ll = LinkedList()
ll.insertion_beginning(11)
ll.insertion_beginning(21)

ll.traversal()
