head = [1, 2, 3, 4]
expected_output = [2, 1, 4, 3]

'''
    Given a linked list, swap every two adjacent nodes and return its head. 
    You must solve the problem without modifying the values in the list's nodes 
    (i.e., only nodes themselves may be changed.)
'''

prev_num = []
for i, num in enumerate(head):
    if i % 2 == 0:
        prev_num.append(num)
        head[i] = head[i+1]

    else:
        head[i] = prev_num[i-2]


print(head)
