def read_grades(gradefile):
    ''' (file open for reading) -> list of float

    Read and return the list of grades in gradefile

    Precondition: gradefile starts with a header that contains
    no blank lines, than has a blank line, and then lines
    containing a student number and a grade.    
    '''

    # Skip over header.
    line = gradefile.readline()
    while line != '\n':
        line = gradefile.readline()

    # Read the grades, accumulating them into a list.

    grades = []
    
    line = gradefile.readline()
    while line != '':
        # Now we have s string
        # containing the info for a single student
        # Find the last space and
        # take everything after that space
        grade = line[line.rfind('  ') + 1:]
        grades.append(float(grade))
        line = gradefile.readline()
        
    return grades

def count_grade_ranges(grades):
    ''' (list of float) -> list of int

    Return a list of int where each index indecates how many grades were
    in these ranges:
    
    0-9: index 0
    10-19:     1
    20-29:     2
    30-39:     3
    40-49:     4
    50-59:     5
    60-69:     6
    70-79:     7
    80-89:     8
    90-99:     9
    100:       10
    >>> count_grade_ranges([78.42, 56.12, 84.34, 60.93, 46.75, 35.28, 78.59, 91.47, 88.92, 47.58, 95.15, 21.32, 68.12, 53.26, 15.46, 92.17, 76.04, 36.29, 82.5, 88.93, 69.49, 57.62, 29.73, 48.65, 80.24, 62.57, 19.45, 98.32, 65.9, 73.18, 38.11, 15.78, 55.73, 42.91, 27.34, 94.52, 63.79, 77.06, 51.17, 45.63, 80.03, 71.24, 12.48, 94.66, 82.95, 89.73, 52.81, 39.58, 58.49, 14.22, 47.11, 33.76, 78.36, 26.27, 49.9, 54.11, 61.95, 85.3, 73.61, 67.84, 19.78, 58.25, 62.17, 47.9, 13.28, 36.5, 89.17, 52.93, 80.5, 75.93, 97.8, 68.63, 77.89, 29.76, 100.0, 74.82, 18.22, 15.64, 93.48, 69.75, 21.9, 37.28, 24.33, 51.1, 49.88, 63.74, 35.81, 92.61, 50.33, 61.67, 47.38, 87.42, 68.81, 33.54, 29.87, 72.66, 38.99, 52.53, 41.71, 100.0, 75.08, 86.99, 69.88, 3.15, 30.57, 45.28, 49.85, 17.93, 82.5, 12.17, 57.99, 49.27, 26.5, 94.74, 32.19, 59.92, 67.31, 44.12, 1.93, 75.17, 27.49, 9.92, 15.93, 74.69, 82.24, 59.35, 100.0, 97.88, 31.4, 6.92, 87.13, 50.19, 68.53, 44.71, 28.43, 80.57, 26.38, 16.74, 63.14, 22.53, 34.71])
    [4, 13, 13, 14, 16, 17, 18, 15, 17, 11, 3]
    '''

    range_counts = [0] * 11

    for grade in grades:
        which_range = int(grade // 10)
        range_counts[which_range] = range_counts[which_range] + 1
    return range_counts


def write_histogram(range_counts, histfile):
    '''(list of int, file open for writing) -> NoneType

    Write a histogram of *'s based on the number of grades in each range.

    The output format:
    
    0-9:   *
    10-19: **
    20-29: *****
    30-39: ******
    40-49: ****
    50-59: *******
    60-69: ********
    70-79: *****
    80-89: ***
    90-99: **
    100:   *
    '''

    histfile.write('0-9:   ')
    histfile.write('*' * range_counts[0])
    histfile.write('\n')

    # Write the 2-digit ranges
    for i in range(1, 10):
        low = i * 10
        high = i * 10 + 9
        histfile.write(str(low) + '-' + str(high) + ': ')
        histfile.write('*' * range_counts[i])
        histfile.write('\n')
    
    histfile.write('100:   ')
    histfile.write('*' * range_counts[-1])
    histfile.write('\n')

    
