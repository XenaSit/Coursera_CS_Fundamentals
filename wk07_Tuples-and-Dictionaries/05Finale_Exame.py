# ==============================================================1===================================
# Select the expression(s) that evaluate to a float value.
# 3 // 4
# 8 + 3

7 + 8.5
3 / 4
8 % 6
3 // 4
# ==============================================================2===================================
x = 2
y = 3 - x
x = 3
# After the code above has been executed, what value does y refer to?
1

a = 7
b = a + 3
a = 9
# After the code above has been executed, what value does y refer to?
10
# ==============================================================3===================================
def f(x):
    y = x * 3
    return y - x
# What value is returned by a call on function f with argument 10?
20
# ==============================================================4===================================
start = 'L'
middle = 8
end = 'R'
# Write an expression that evaluates to the string 'L8R' using only the variables start, middle, end, 
# one call on function str, and string concatenation.
# Do not use unnecessary parentheses: you need them for the function call, but nothing else.
start + str(middle) + end

# ==============================================================5===================================
def count_max_letters(s1, s2, letter):
    '''(str, str, str) -> int 
    s1 and s2 are strings, and letter is a string of length 1.     Count how manytimes letter appears in s1 and in s2, and ret    urn the bigger of the twocounts.
    >>> count_max_letters('hello', 'world', 'l')
    2
    >>> count_max_letters('cat', 'abracadabra', 'a')
    5
    '''
    return # CODE MISSING HERE

# The expression for the return statement is missing.  Write that expression below.  
# Use only the parameters, one call on function max, and two calls on str method count.
# Do not use unnecessary parentheses: you need them for the function and method calls, but nothing else.  
# Do not include the word return; just write the expression.

max(s1.count(letter), s2.count(letter))

# ==============================================================6===================================
def same_length(L1, L2):
    '''(list, list) -> bool
    Return True if and only if L1 and L2 contain the same number of elements.
    '''
    if len(L1) == len(L2):
       return True
    else:
       return False
# The function works, but the if statement can be replaced with a single return statement:
# return # CODE MISSING HERE\
# Write the missing expression.  Use only the parameters, two calls on function len, and operator == once.
# Do not use unnecessary parentheses: you need them for the function calls, but nothing else.  
# Do not include the word return; just write the expression.
len(L1) == len(L2)

# ==============================================================7===================================
# Consider these two functions; we provide only the headers, type contracts, and a precondition:
def moogah(a, b):
    '''(str, int) -> str'''

def frooble(L):
    '''(list of str) -> int
    Precondition: L has at least one element.'''

# Below are code fragments that call these two functions in various ways.  
# Select the code fragment(s) below that are valid according to the function headers and the type contracts.

# (a) moogah(frooble(['a']), 'a')
# (c) frooble(moogah('', 0))

# CORRECT answer:
# (d) lst = ['a', 'b', 'c']
# moogah(lst[0], len(lst))

# (b) frooble([moogah('', 0)])

# ==============================================================8===================================
def reverse(s):
    '''(str) -> str
    Return the reverse of s.
    >>> reverse('abc')
    'cba'
    >>> reverse('a')
    'a'
    >>> reverse('madam')
    'madam'
    >>> reverse('1234!')
    '!4321'
    '''
#    result = ''
#    i = len(s) - 1
#    while i >= 0:
#         result = result + s[i]
#         i = # CODE MISSING HERE

#    return result
# Write the missing expression.  Do not use parentheses.  Do not include " i =". Just write the missing expression.
i  - 1
# ==============================================================9===================================
def get_keys(L, d):
    '''(list, dict) -> list

    Return a new list containing all the items in L that are keys in d.

    >>> get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'})
    [1, 'a']
    '''
  
    # result = []
    # for # CODE MISSING HERE
    #    if k in d:
    #       result.append(k)

    # return result

# Write the missing code for the first line of the for loop — everything after the word "for", 
# up to and including the colon :.
# Do not use any parentheses, and do not call any functions or methods.
# k in L:
# ==============================================================10==================================
def count_values_that_are_keys(d):
    '''(dict) -> int

    Return the number of values in d that are also keys in d.
   
    >>> count_values_that_are_keys({1: 2, 2: 3, 3: 3})
    3
    >>> count_values_that_are_keys({1: 1})
    1
    >>> count_values_that_are_keys({1: 2, 2: 3, 3: 0})
    2
    >>> count_values_that_are_keys({1: 2})
    0
    '''

    # result = 0
    # for k in d:
    #     if # CODE MISSING HERE
    #          result = result + 1

    # return result
# Write the missing code for the if statement — everything after the word "if", up to and including the colon :.
# Your answer should only use operator in, variables k and d, and indexing.
d[k] in d



def are_lengths_of_strs(L1, L2):
    '''(list of int, list of str) -> bool
  
    Return True if and only if all the ints in L1 are the lengths of the strings
    in L2 at the corresponding positions.

    Precondition: len(L1) == len(L2)

    >>> are_lengths_of_strs([4, 0, 2], ['abcd', '', 'ef'])
    True
    '''

#    result = True
#    for i in range(len(L1)):
#        if # CODE MISSING HERE
#             result = False

#    return result

# Write the missing code for the if statement — everything after the word " if", up to and including the colon :.

# Your answer should be of the form expr1 != expr2:, where expr1 and expr2 are expressions.  
# Use only variables i, L1, L2, indexing, and function len.

# Do not use parentheses except for the call on len.
# len(L2[i]) != L1[i]:

# ==============================================================11=WRONG=================================
# def double_values(collection):
#     for v in range(len(collection)):
#          collection[v] = collection[v] * 2
# Strings, tuples, lists, and dictionaries can all be iterated over, and function len works with all of them.

d = {0: 10, 1: 20, 2: 30}
double_values(d)

d = {0: 10, 1: 20, 2: 30}
double_values(d)

# s = '123'
# double_values(s)

t = (1, 2, 3)
double_values(t)

d = {1: 10, 2: 20, 3: 30}
double_values(d)
# ==============================================================12=WRONG=================================
# The diagonal of a square nested list goes from the top-left to the bottom-right corner.  
# For example, consider this square nested list:

# [[1, 3, 5], [2, 4, 5], [4, 0, 8]]

# That nested list represents this table, where the values on the diagonal are in bold:

#  1  3  5

#  2  4  5

#  4  0  8

def get_diagonal_and_non_diagonal(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the values on the
    diagonal of square nested list L and the second item is a list of the rest
    of the values in L.

    >>> get_diagonal_and_non_diagonal([[1,  3,  5], [2,  4,  5], [4,  0,  8]])
    ([1, 4, 8], [3, 5, 2, 5, 4, 0])
    '''

    # diagonal = []
    # non_diagonal = []
    # for row in range(len(L)):
    #     for col in range(len(L)):

            # CODE MISSING HERE

    # return (diagonal, non_diagonal)

            # if row == col:
            #     diagonal.append(L[row][row])
            # else:
            #     non_diagonal.append(L[row][col])

            # if row == col:
            #     diagonal.append(L[row][col])
            # else:
            #     non_diagonal.append(L[row][col])


            # if row == col:
            #     diagonal.append(L[row][col])
            # if row != col:
            #     non_diagonal.append(L[row][col])


            # if row == col:
            #     diagonal.append(L[row][col])
            # elif row != col:
            #     non_diagonal.append(L[row][col])



            # if row == col:
            #     diagonal.append(L[row][col])

            # non_diagonal.append(L[row][col])                                





def get_negative_nonnegative_lists(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the negative ints in the
    inner lists of L and the second item is a list of the non-negative ints
    in those inner lists.

    Precondition: the number of rows in L is the same as the number of
    columns.

    >>> get_negative_nonnegative_lists([[-1,  3,  5], [2,  -4,  5], [4,  0,  8]])
    ([-1, -4], [3, 5, 2, 5, 4, 0, 8])
    '''

    # nonneg = []
    # neg = []
    # for row in range(len(L)):
    #     for col in range(len(L)):
    #         # CODE MISSING HERE

    # return (neg, nonneg)


            # if L[row][col] < 0:
            #     nonneg.append(L[row][col])
            # else:
            #     neg.append(L[row][col])


            # if L[row][col] > 0:
            #     nonneg.append(L[row][col])
            # else:
            #     neg.append(L[row][col])


            # if L[row][col] < 0:
            #     neg.append(L[row][col])
            # else:
            #     nonneg.append(L[row][col])                


            # if L[row][col] < 0:
            #     neg.append(L[row][col])

            # nonneg.append(L[row][col])


            # val = L[row][col]
            # if val < 0:
            #     neg.append(val)
            # else:
            #     nonneg.append(val)
# ==============================================================13================================== 


def count_chars(s):
    '''(str) -> dict of {str: int}

    Return a dictionary where the keys are the characters in s and the values
    are how many times those characters appear in s.

    >>> count_chars('abracadabra')
    {'a': 5, 'r': 2, 'b': 2, 'c': 1, 'd': 1}
    '''
    d = {}

    # for c in s:
    #     if not (c in d):
    #         # CODE MISSING HERE
    #     else:
    #         d[c] = d[c] + 1

    # return d


d[c] = 1