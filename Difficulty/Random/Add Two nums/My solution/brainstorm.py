l1 = [2, 4, 3]
l2 = [5, 6, 4]

def add_nums(_list):
    length = len(_list)
    sum = 0
    while length > 0:
        x = ((_list[length - 1] * (10) ** (length - 1)))
        sum += x
        length -= 1

    return sum

def sum_to_reversed_list(n):
    output = []
    while n > 0:
        r = n % 10
        output.append(r)
        n = n // 10
    return  output


sum_l1=add_nums(l1)
sum_l2=add_nums(l2)

n=sum_l1+sum_l2
print(sum_to_reversed_list(n))


