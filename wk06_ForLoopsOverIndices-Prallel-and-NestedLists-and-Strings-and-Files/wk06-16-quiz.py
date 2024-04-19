# ======================3========================== only one answer
def mystery(s):
    ''' (str) -> bool
    '''
    matches = 0
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - 1 - i]:
            matches = matches + 1

    return matches == (len(s) // 2)

# Which is the best docstring description for function mystery?
# Return True if and only if s[:len(s) // 2]  is the same as s[len(s) // 2:].
# Return True if and only if the number of duplicate characters in s is equal to len(s) // 2.
# Return True if and only if s is equal to the reverse of s.
# Return True if and only if there are exactly len(s) // 2 characters in s that are the same character.

# ======================4==========================only one answer

# 4. In one of the Week 6 lecture videos, we wrote the function shift_left. Consider this function, which shifts in the other direction:
# Select the code fragment that correctly completes function shift_right.
# Hint: the correct answer works from the end to the beginning of L.


    for i in range(1, len(L)):
        L[len(L) - i] = L[len(L) - i - 1]

# ======================9==========================more than one

def contains(value, lst):
    ''' (object, list of list) -> bool
  
   Return whether value is an element of one of the nested        lists in lst.

   >>> contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'],    [80, 100]])
   True
   '''

'''
   Found = False  # We have not yet found value in the list.

   # CODE MISSING HERE
   
   return found'''

# Select the code fragment(s) that make the function above match its docstring description.


#     for i in range(len(lst)):
#         for j in range(len(lst[i])):
#             if lst[i][j] == value:
#                 found = True

#     for sublist in lst:
#         if value in sublist:
#             found = True

# ======================12==========================more than one

def lines_startswith(file, letter):
     ''' (file open for reading, str) -> list of str

     Return the list of lines from file that begin with letter.     The lines should have thenewline removed.

    Precondition: len(letter) == 1

    matches = []

    # CODE MISSING HERE

    return matches
    '''


# Select the code fragment(s) that make the function above match its docstring description.


#     for line in file:
#         if letter == line[0]:
#             matches.append(line.rstrip('\n'))



#     for line in file:
#         if line.startswith(letter):
#             matches.append(line.rstrip('\n'))

#     for line in file:
#         if letter in line:
#             matches.append(line.rstrip('\n'))

#     matches.append(line.startswith(letter).rstrip('\n'))






