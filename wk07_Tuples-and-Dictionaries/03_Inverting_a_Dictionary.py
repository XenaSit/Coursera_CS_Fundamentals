fruit_to_colour = {
    'watermelon': 'green', 
    'pomegranate': 'red',
    'peach': 'orange', 
    'cherry': 'red', 
    'pear': 'green',
    'banana': 'yellow', 
    'plum': 'purple', 
    'orange': 'orange'}

for fruit in fruit_to_colour:
    print (fruit, fruit_to_colour[fruit])

'''
watermelon green
pomegranate red
peach orange
cherry red
pear green
banana yellow
plum purple
orange orange
'''

colour_to_fruit = {}
for fruit in fruit_to_colour:
    colour = fruit_to_colour[fruit]
    colour_to_fruit[colour] = fruit

'''
fruit_to_colour
{'watermelon': 'green', 'pomegranate': 'red', 'peach': 'orange', 'cherry': 'red', 'pear': 'green', 'banana': 'yellow', 'plum': 'purple', 'orange': 'orange'}
colour_to_fruit
{'green': 'pear', 'red': 'cherry', 'orange': 'orange', 'yellow': 'banana', 'purple': 'plum'}
'''

'''
If the colour is not a key in the dictionary, add it with 
its value being a single element a list consisting of the fruit.
If the colour is already a key, append the fruit to the list of fruit associated with that key.
'''

colour_to_fruit = {}
for fruit in fruit_to_colour:
    # What colour is the fruit?
    colour = fruit_to_colour[fruit]
    if not (colour in colour_to_fruit):
        colour_to_fruit[colour] = [fruit]
    else:
        colour_to_fruit[colour].append(fruit)

'''
>>> colour_to_fruit
{
    'orange': ['peach', 'orange'], 
    'purple': ['plum'], 
    'green': ['watermelon', 'pear'], 
    'yellow': ['banana'], 
    'red': ['cherry', 'pomegranate']}

    TO GET TO STUFF:
    >>> colour_to_fruit['orange']
    ['peach', 'orange']
    >>> colour_to_fruit['orange'][0]
    'peach'
'''

