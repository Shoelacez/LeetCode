import math

head = [1, 2, 3, 4, 5]
k = 3
expected_output = [2, 1, 4, 3, 5]

partitions = len(head)/k
# print(head[:k])
# print(head[k:2*k])
# print(head[2*k:3*k])

output = []
for i,n in enumerate(range(math.ceil(partitions))):
    start = k*i
    end = k*(i+1)
    portion = head[start: end]

    '''Reverse the portion'''
    portion.sort(reverse=True)

    output.append(portion)
    # print(portion)


# print(output)

def unpack_the_output(iterable):
    final_result = []
    for l in iterable:
        for n in l:
            final_result.append(n)

    print(final_result)



unpack_the_output(output)