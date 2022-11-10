word = input("Word: ")

def checkPalindrome(word):
    palindrome = False
    counter = 1
    new_string = ''
    while counter <= len(word):
        t = word[-1 * counter]
        new_string += t
        counter += 1
    if (new_string == word):
        palindrome = True
    return palindrome


palindromes=[]
new_string = ''
for c in word:
    new_string=''
    # print(f"Case {c}")
    for char in word[word.index(c):]:
        new_string+=char
        # print(new_string)
        eval = checkPalindrome(new_string)
        # print(eval)

#         In cae it is a palindrome
        if eval:
            # ignoring the single letters
            if len(new_string) == 1:
                continue
            # print(f"{new_string}, length: {len(new_string)}")

            if new_string in palindromes:
                pass
            else:
                palindromes.append(new_string)


print(palindromes)






'''1. i need to iuse real incies and not str.index()'''