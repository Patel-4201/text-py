def reverse_char(char):
    """
    Reverse a character either lower or capital!
    """
    # define
    alphabets = 'abcdefgfijklmnopqrstuvwxyz'
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
    pass
print("hello")