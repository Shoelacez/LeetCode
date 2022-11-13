list1 = [1, 2, 4]
list2 = [1, 3, 4]

expected_output = [1, 1, 2, 3, 4, 4]
output = []

for item1, item2 in zip(list1, list2):
    output.append(item1)
    output.append(item2)

print(output)


'''Gotta learn about Singly linked lists on python'''
class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list.listprint()