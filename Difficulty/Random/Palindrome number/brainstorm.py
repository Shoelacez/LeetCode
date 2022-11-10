n = -121
positive = True
def reverse_num(number):
    # check if neg
    if number < 0:
        print("False")
        positive =False
        reversed_number = 0
    else:
        rev_num=[]
        while number != 0:
            rem = number%10
            rev_num.append(rem)
            number=number//10

        reversed_number=0
        for index, n in enumerate(rev_num):
            place_vals=rev_num[-1*(index+1)]*10**index
            reversed_number+=place_vals
    return reversed_number

reversed_number=reverse_num(n)

def check_palindrome(number, rev_num):
    if rev_num == number and positive:
        print("True")
    else:
        print(f"not a palindrome because number={number} and reversed={rev_num}")

check_palindrome(n, reversed_number)