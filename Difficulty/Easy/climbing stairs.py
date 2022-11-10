'''
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps.
    In how many distinct ways can you climb to the top?
'''
n = 4
highest_step = 2

possibilities = []
for n in range(1, highest_step+1):
    print(f"Case {n}")
    for num in range(1, n+1):
        print(num)
