grades = [['Assignment 1', 80], ['Assignment 2', 90], ['Assignment 3', 70]]
'''
    >>>len(grades)
    3
    
    >>>grades[0]
    ['Assignment 1', 80]
    
    >>>len(grades[0])
    2

    >>> for item in grades:
            print(item)
            
    ['Assignment 1', 80]
    ['Assignment 2', 90]
    ['Assignment 3', 70]

    >>> grades[0][0]
    'Assignment 1'
    >>> grades[1][1]
    90
    '''
def calculate_average(asn_grades):
    ''' (list of list of [str, number]) -> float
    Return the average of the grades in asn_grades.

    >>> calculate_average([['A1', 80], ['A2', 90], ['A3', 70]])
    85.0
    '''

    total = 0

    for item in asn_grades:
        total = total + item[1]

    return total / len(asn_grades)

'''
for i in range(10, 13):
    for j in range(1, 5):
        print(i, j)

    OUTPUT
    10 1
    10 2
    10 3
    10 4
    '''





