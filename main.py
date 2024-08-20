def reverse_char(char):
    """
    Reverse a character either lower or capital!
    """
    # define alpha
    alphabets = 'abcdefgfijklmnopqrstuvwxyz'
    # return char if not valid alphabet
    if char not in alphabets and char not in alphabets.upper():
        return char
    
    # upper case
    if char in alphabets.upper():
        alphabets = alphabets.upper()
    # find index of char
    index_of_char = alphabets.index(char)
    # opposite index
    opposite_index = 26 - index_of_char
    # - 1 oppo index
    oppo_char = alphabets[opposite_index - 1]
    return oppo_char
x= reverse_char('X')
print(x)


def atbash(txt):
    reverseTxt=""
    for char in txt:
        reverseTxt += reverse_char(char)
    return reverseTxt

print(atbash("Hello world!") == "Svool dliow!")

