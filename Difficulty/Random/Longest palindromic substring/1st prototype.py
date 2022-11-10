word = 'babad'
new_string = ''
palindromes=[]

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



for c in word:
    print(f"Case {c}")
    for char in word[word.index(c):]:
        new_string+=char
        print(new_string)
        eval = checkPalindrome(new_string)
        print(eval)


