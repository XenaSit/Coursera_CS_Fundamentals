<h1>range</h1>

<h3>The Built-in Function: range</h3>

    Python has a built-in function called range that is useful to use when you want to generate a sequence of numbers. You can type help(range) in IDLE if you ever need a reminder.

The example below will print the integers 0 to 9, inclusive.

    for i in range(10):
        print (i)

The form of range is:

    range([start,] stop[, step]):
        return a virtual sequence of numbers from start to stop by step
			
<h3>Applications of Range</h3>

There are other options you can specify to range. One option is to let range generate the numbers corresponding to indices of a string or a list.

    s = 'computer science'
    for i in range(len(s)):
        print(i)

You can also tell range what index to start at. For instance, the example below starts at index 1 (as opposed to the default which is 0).

    for i in range(1, len(s)):
        print(i)

You can even specify the "step" for range. The default stepping size is 1, which means that numbers increment by 1. The example below starts at index 1 and its step size is there (goes to every third index).

    for i in range(1, len(s), 3):
        print(i)