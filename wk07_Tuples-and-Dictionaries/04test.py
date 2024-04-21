# ==============================================================1==================================
>>> d = {'a': 1, 'b': 2}
>>> # CODE MISSING HERE
>>> d
{'a': 1, 'c': 3, 'b': 2}
Write the missing assignment statement that that modifies the dictionary as shown. 
(Just write the assignment statement; don't write the >>> part.)
d['c'] = 3

# ==============================================================2==================================
>>> d = {'a': 1, 'b': 2}
>>> # CODE MISSING HERE
>>> d
{'a': 1, 'b': 3}
Write the missing assignment statement that modifies the dictionary as shown. (Just write the assignment statement; don't write the >>> part.)
d['b'] = 3



# ==============================================================3==================================
>>> d = {'a': [1, 3], 'b': [5, 7]}
# CODE MISSING HERE
>>> d
{'a': [1, 2, 3], 'b': [5, 7]}
Select the option(s) that would lead to this result. Hint: call help on insert, append, and sort.

# d['a'].append(2)
# d[’a’].sort()

# d[’a’].append(2)

d['a'].insert(1, 2)
# ==============================================================4==================================
d = {'a': 1, 'c': 3, 'b': 2}
Select the expression(s) that evaluate to True.
"b" in d
not ('e' in d)






# ==============================================================5==================================
d = {'a': [1, 3], 'b': [5, 7, 9], 'c': [11]}
Select the expression(s) that evaluate to 3.
len(d['a']) + len(d['c'])
len(d)
# len(d['a' + 'c']) no
&&
len(d'’b''])
len(d)



# ==============================================================6==================================
tup = (1, 2, 3)
Select the expression(s) and statement(s) below that result in an error.
# tup[-2] = 4
# tup.reverse()
# tup[0:2] == (10, 30)

# tup[0] == tup[-1]
# tup.append(4)

tup[-2] = 4
tup.reverse()
# ==============================================================7==================================
Select the expression(s) that can be used as dictionary keys.
('single',)
(1, 'fred', 2.0)


# ==============================================================8==================================
d = {1: ['a', 'b', 'c'], 2: ['d', 'e'], 3: []}
Select the code fragment(s) that set variable total to the number of items in all the lists that occur 
as values in d.

# L = []
# for k in d:
#     L.append(k)

# total = len(L)
# ======================
# total = 0
# for k in d:
#     total = total + k
# =====================
# =====================
# =====================
# total = 0
# for k in d:
#     total = total + k
# =====================
# total = 0
# for k in d:
#     total = total + len(d[k])
=====================
=====================
=====================
L = []
for k in d:
    L.append(k)

total = len(L)
=====================
total = 0
for k in d:
    total = total + len(d[k])



# ==============================================================9==================================
This dictionary has 3 keys that are all the same. Enter this in the Python shell:
Submit what the code above evaluates to; don't submit your answers to the thought questions below.

What we want you to think about: We haven't covered this situation in the videos; what do you think should happen? 
Do you think this should this cause an error? 
Should it discard some of the key/value pairs? 
If so, which one do you think it should keep? 
People who create programming languages have to make these kinds of decisions, 
and often there isn't a clear good choice.
{1: 30}








# ==============================================================10==================================
L = [['apple', 3], ['pear', 2], ['banana', 3]]
d = {}
for item in L:
   d[item[0]] = item[1]
What does this code do?
# Reorders the items in the inner lists of L.

# Removes the items from L and populates dictionary d where each key is the first item of each inner list of 
# L and each value is the second item of that inner list.


Populates dictionary d where each key is the first item of each inner list of 
L and each value is the second item of that inner list.






# ==============================================================11==================================
def eat(d):
    '''(dict of {str: int}) -> bool

    Each key in d is a fruit and each value is the quantity of     that fruit.

    REST OF DESCRIPTION MISSING HERE

    >>> eat({'apple': 2, 'banana': 3, 'pear': 3, 'peach': 1})
    True
    >>> eat({'apple': 0, 'banana': 0})
    False
    '''
    ate = False
    for fruit in d:
        if d[fruit] > 0:
            d[fruit] = d[fruit] - 1
            ate = True

    return ate


Try to eat one of each fruit: reduce by 1 all quantities greater than 0 associated with each fruit in d and return 
True if and only if any fruit was eaten.








# ==============================================================12==================================
def contains(v, d):
    ''' (object, dict of {object: list}) -> bool

    Return whether v is an element of one of the list values in    d.
    >>> contains('moogah', {1: [70, 'blue'], 2: [1.24, 'moogah'    , 90], 3.14: [80, 100]})
    True
    >>> contains('moogah', {'moogah': [1.24, 'frooble', 90], 3.    14: [80, 100]})
    False
    '''

    found = False # Whether we have found v in a list in d.

    # CODE MISSING HERE
 
    return found
Select the code fragment(s) that make the function above match its docstring description.

    # for k in d:
    #     if v == k:
    #         found = True

    # for k in d:
    #     if v in d[k]:
    #         found = True

====================================
    # for k in d:
    #     for i in range(len(d[k])):
    #         if d[k][i] == v:
    #             found = True
    # for k in d:
    #     for i in range(len(d[k])):
    #         found = (d[k][i] == v)

====================================
    for k in d:
        if v == k:
            found = True

    for k in d:
        for i in range(len(d[k])):
            if d[k][i] == v:
                found = True