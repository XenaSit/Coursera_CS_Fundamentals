def fruit_color(fruit):
    if fruit == 'apple':
        return 'red'
    elif fruit == 'banana':
        return 'yellow'
    elif fruit == 'pear':
        return 'green'

print(fruit_color('apple'))

def traffic_report(light):
    if light == 'red':
        return 'stop'
    elif light == 'yellow':
        return 'slow'
    elif light == 'green':
        return 'go'

print(traffic_report('orange'))


def grade_report(grade):
    if grade >= 80:
        return 'excellent'
    elif grade >= 50:
        return 'pass'

Question 13 grade1 and grade2represent two grades (floats) between 0.0 and 100.0, inclusive. A passing grade is greater than or equal to 50.   Select the code fragment(s) that prints the average of all passing grade(s). The printed value should be 0.0 if neither grade is a passing grade, the passing grade if exactly one grade is a passing grade, and the average of the two grades if both are passing grades.

Watch your ifs and elifs!
NUMBER 1
total = 0
grade_count = 0

if grade1 >= 50:
    total = total + grade1
    grade_count = grade_count + 1
if grade2 >= 50:
    total = total + grade2
    grade_count = grade_count + 1

if grade_count > 0:
    print(total / grade_count)
else:
    print(0.0)


NUMBER 2
total = 0
grade_count = 0

if grade1 >= 50 and grade2 >= 50:
    total = grade1 + grade2
    grade_count = 2

if grade_count > 0:
    print(total / grade_count)
else:
    print(0.0)

NUMBER 3
total = 0
grade_count = 0

if grade1 >= 50:
    total = total + grade1
    grade_count = grade_count + 1
else:
    total = total + grade2
    grade_count = grade_count + 1

if grade_count > 0:
    print(total / grade_count)
else:
    print(0.0)

NUMBER 4
total = 0
grade_count = 0

if grade1 >= 50:
    total = total + grade1
    grade_count = grade_count + 1
elif grade2 >= 50:
    total = total + grade2
    grade_count = grade_count + 1

if grade_count > 0:
    print(total / grade_count)
else:
    print(0.0)
