# Introduction
You do not need to know much Python to do these assignments, the more you know, the easier it will be.

# Comments
In Python you need to see lines like:

`# This line does X with Y`

These lines are for documentation, the first line of defense for keeping your code easy to understand. There are whole books about how to write effective comments, but all you need to know is that it makes everything after it not executed as code. You can have it on a seperate line like above, or at the end of a line like this:

`print("Hello world!") # Output the value to the console`

Everything past the hashmark will not be executed.

# Variables
Variables are a way to store information temporarily for reference later. Use as many as you want, some people try to optimize for these, but in high-level languages, especially for learning it's better to be explicit. 

`variable_name = 4`
`variable_2 = 5 + 8`

Variable names cannot start with a number, and must contain no spaces. Typically, in python you use\_underscores\_to\_ show a variable name. All lower case.

If you want to reference this variable later you can just use it's name:

`variable_3 = variable_2 * 320`

# Arithmetic Operators
Arithmetic operators are things like addition (`+`), subtraction(`-`), multiplication(`*`), division(`/`) and modulus(`%`).

You can use them like you'd expect:
`added_value = 3 + 4 # Equals 7`
`subtracted_value = 3 - 4 # Equals -1`
`multiplied_value = 3 * 4 # Equals 12`
`divided_value = 3 / 4 # Equals 0.75`
`remaining_value = 4 % 3 # Equals 1`

Now, you may be thinking... modulus? What the fuck is that. It's basically a type of division. But instead of returning how many of value A can fit into value B. It returns the remainder of the division between value A and B.
`mod_1 = 12 % 5 # Equals 2`
`mod_1 = 9 % 3 # Equals 0`
`mod_1 = 20 % 11 # Equals 9`
`mod_1 = 7 % 6 # Equals 1`
`mod_1 = 10 % 5 # Equals 0`

It can be very helpful in math problems. So it's good to know. You can also use brackets in arithmetic:

`bracket_example = ((4 + 5) * 75) % 39`

# Comparison Operators
Now with arithmetic operators you also get a number as the results `4 + 5` will always return `9`. However, there is another class of operators that take in values like numbers and letters and instead of returning a number, it returns `True` or `False` which can be helpful for making decisions in a program.

The double equals sign `==` checks to see if two numbers are equal.

`variable1 = (4 == 4) # Returns True`
`variable2 = (4 == 3) # Returns False`

And remember that variables can be used instead of numbers in any example:

`variable3 = (4 == value_stored)`

There are also a number of other comparrison operators:
Not equals: `variable = (4 != 5) # Returns True`
Greater than: `variable = (5 > 4) # Returns True`
Less than: `variable = (22 < 190) # Returns False`
Greater than or equal: `variable = (25 >= 25) # Returns True`
Less than or equal: `variable = (18 <= 30) # Returns True`

# Conditional Statements
Conditional statements use the comparison operators to decide whether or not to run a section of code. The typical keyword to start an conditional statement is `if` you use this structure: `if [COMPARISON]:` the value for [COMPARISON] is one of the comparison operators we just looked at. All the code you want to have run if the comparsion turns out to be `True` will be undernether the statement and **indented** this is important, this is how python knows to keep your code in executing properly. So press Tab to indent for everything you want to be conditional:

```python
if [COMPARISON]:
    # This code runs if true
    # This code will also run

# This code will always run, no matter what happens with the if statement.

```


For instance, this code will always run, because `40 == 40` is always `True`:

```python
if 40 == 40:
    value_2 = 75
    # Do other stuff here
```

However, the code in this if statement never runs:

```python
if 40 == 40:
    value_2 = 75
    # Do other stuff here
```

There is also a way to tell Python to do something special if it turns out the statement is `False`, the `else` keyword says that code will run only if the if statement is false. This way you can handle both conditions.

```python
if variable > 30:
    output_string = "Value is greater than 30."
else:
    output_string = "Value is less than or equal to 30."
```

# Functions
Functions are a peice of reusable code that you have named, kind of like a variable, but for whole sections of code. They are made using the `def` keywords like this:

```python
def function1():
    return 5 + 20
```

The `()` followed by a `:` is also required. Typically the function has set inputs and output. The output is placed after the keyword `return` in the function. This can be used multiple times. But once the first one is executed, the function will stop running anymore code.

```python
def function1():
    return 98
    return 44
```

That code will always return only `98`. You can have inputs set in the `()` we mentioned earlier, seperate differnt inputs with a comma:

def function2(value1, value2):
    return (value1 * value2) + 89

Now, when you `def` or define a function, the code doesn't actually run right away you need to `call` the function. This is done by using it's name and the `()` with any inputs filled in (if required). You always need to include the brackets, even if they are empty. It's how you tell Python that it is a function and not a variable.

```python
value1 = function1()
value2 = function2(4, 10)
```

Now these variables contain the values `return`ed from the function. A function can return a number, a string (which are words contained in quotes like "Hello there, I'm Mackie!"), boolean values (True, or False), and even more complex objects we probably won't talk about today.

Python even has some built in functions that you don't have to define.

# Input
You can take input from the command prompt by using the built-in function `input()` like so:

```python
user_input1 = input()
user_input1 = input()
added_values = user_input1 + user_input2
```

The program will be paused while it waits for input.

You can also add a `prompt` to ask users what you want them to input:

```python
user_input1 = input("Please enter a value: ")
```

# Output
Outputting a value to command prompt is great for debugging or for a final display. You can use the built-in function `print()` where you put a value to output to console.

```python
value1 = 455
print("This will be printed!") # Output: This will be printed!
print(value1) # Output: 455
print("Value is " + value 1) # Output: Value is: 455
```

As you can see you can also add string and variables together to build text that can change depending on the state of the program. See this little calculator that adds and subtracts:

```python
value1 = input("Enter number: ")
value2 = input("Enter number: ")
operator = input("Enter + or - for calculator function: ")

if operator == "+":
    added = value1 + value2
    print(added)

if operator == "-": 
    subtracted = value1 - value2
    print(subtracted)
```

# Conclusion

I'm sure I've forgotten some things. Google is your best friend in this! Email me if you have questions.
