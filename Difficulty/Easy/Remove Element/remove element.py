'''APPROACH 1'''
#  打印02 and i have no clue on wg=hat is going on.

# Initialization
counter = 1
num = 1
total  = 0

# Reading the numbers from the user
while num > 0:
    num = int(input(f"Num {counter}: "))
    counter += 1
    total += num

print(total - num)


