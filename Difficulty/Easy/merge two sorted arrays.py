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
            print(printval.dataval)
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

'''03'''
# Python program to merge two sorted arrays/
def mergeArrays(arr1, arr2, n1, n2, arr3):
	i = 0
	j = 0
	k = 0

	# traverse the arr1 and insert its element in arr3
	while(i < n1):
		arr3[k] = arr1[i]
		k += 1
		i += 1

	# now traverse arr2 and insert in arr3
	while(j < n2):
		arr3[k] = arr2[j]
		k += 1
		j += 1

	# sort the whole array arr3
	arr3.sort()


# Driver code
if __name__ == '__main__':
	arr1 = [1, 3, 5, 7]
	n1 = len(arr1)

	arr2 = [2, 4, 6, 8]
	n2 = len(arr2)

	arr3 = [0 for i in range(n1+n2)]
	mergeArrays(arr1, arr2, n1, n2, arr3)

	print("Array after merging")
	for i in range(n1 + n2):
		print(arr3[i], end=" ")

# This code is contributed by Tapesh(tapeshdua420)

