'''
    len('mom') in [1, 2, 3] // true
    len([1, 2, 3]) == len(['a', 'b', 'c']) // true

    '3' in [1, 2, 3] // false
    'a' in ['mom', 'dad'] // false
    [1, 2, 3] in len('mom') // false

    int('3') in [len('a'), len('ab'), len('abc')] // true
    '''
def mystery(s):
    '''
    mystery('abc') // yes
    mystery('123') //no
    mystery('abc123') //no
    mystery('123abc') //no
    '''
    i = 0
    result = ''

    while not s[i].isdigit():
          result = result + s[i]
          i = i + 1

    return result




def example(L):
    '''(list) -> list
    Return a list containing the items from L starting from index 0, omitting every third item.
    Return an empty list.
    Return a list containing every third item from L starting at index 0. //YYY
    Return a list containing every third index from L starting at index 0.
    '''
    i = 0
    result = []
    while i < len(L):
        result.append(L[i])
        i = i + 3
    return result



def compress_list(L):
    '''(list of str) -> list of str

    Return a new list with adjacent pairs of string elements
    from Lconcatenated together, starting with indices 0 and 1,
    2 and 3,and so on.

    Precondition: len(L) >= 2 and len(L) % 2 == 0

    >>> compress_list(['a', 'b', 'c', 'd'])
    ['ab', 'cd']

    i = i * 2
    i = i + i
    i = i + 2 YYY
    i = i + 1
    
    compressed_list = []
    i = 0

    while i < len(L):
        compressed_list.append(L[i] + L[i + 1])
        # MISSING CODE HERE

     return compressed_list
    

print (sum(range(1523, 10504, 2))) // 27004383
print (sum(range(524, 10508 + 1, 2))) // 27541388

def while_version(L):
    (list of number) -> number
    
    i = 0
    total = 0

    while i < len(L) and L[i] % 2 != 0:
        total = total + L[i]
        i = i + 1

    return total
    '''
'''
def increment_items(L, increment):
    i = 0
    while i < len(L):
        L[i] = L[i] + increment
        i = i + 1

values = [1, 2, 3]
print(increment_items(values, 2))
print(values)

None
[3, 4, 5]
'''

'''
a = [1, 2, 3]
b = a


(a)
    a = [1, 'A', 3]
    b = [1, 'A', 3]
(b)
    b[1] = ’AB’
    a[1] = a[1][0]
(c)
    a[1] = 'A'
(d)
    b[-2] = ’A’

print(a, b)
'''


def cap_song_repetition(playlist, song):
    '''(list of str, str) -> NoneType
    ['Lola', 'Venus', 'Lola', 'Lola', 'Let It Be', 'Lola', 'ABC', 'Cecilia', 'Lola', 'Lola']
    Make sure there are no more than 3 occurrences of song in playlist.

    '''
    while playlist.count(song) > 3:
        playlist.remove(playlist.index(song))
