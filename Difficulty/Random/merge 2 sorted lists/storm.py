lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
expected_output: [1, 1, 2, 3, 4, 4, 5, 6]
'''
    Explanation: The linked-lists are:
    [
      1->4->5,
      1->3->4,
      2->6
    ]
    merging them into one sorted list:
    1->1->2->3->4->4->5->6
'''

single_list = []
for l in lists:
    for inner_list in l:
        single_list.append(inner_list)

single_list.sort()
print(single_list)
