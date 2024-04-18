def shift_left(L):
    ''' (list) -> NoneType

    Shift each item in L one position to the left
    and shift the first item to the last position.

    Precondition: len(L) >= 1
    >>> shift_left(['a', 'b', 'c', 'd'])
    L = ['a', 'b', 'c', 'd']
    shift_left(L)
    print(L)
    OUTPUT
    ['b', 'c', 'd', 'a']

    letters = ['a', 'b', 'c', 'd']
    print(shift_left(letters))
    print (letters)
    '''
    
    first_item = L[0]

    for i in range(1, len(L)):
        L[i - 1] = L[i]

    L[-1] = first_item      

    

def count_adjacent_repeats(s):
    ''' (str) -> int

    Return the number of occurrences of a character and
    an adjacent character being the same.

    >>> count_adjacent_repeats('abccdeffggh')
    3
    '''

    repeats = 0

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            repeats = repeats + 1

    return repeats

# Class Examples ==========================================
s = 'wepoi'
for i in range(len(s) - 1):
    print(i)\
# OUTPUT
# 0
# 1
# 2
# 3
