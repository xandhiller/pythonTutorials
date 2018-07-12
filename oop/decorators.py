# This builds on the work in the closures.py file and on the concept of a closure.

# Going to tweak the function, so recopying it.
def outer_func(msg):
    def inner_func():
        print(msg)
    return inner_func

# Taking the idea of a closure, we can make a simple decorator.
def decorator_func(original_function):
    def wrapper_func():
        return original_function()
    return wrapper_func

# In this ^ function we are passing in some original function, and then returning it when called on the assigned variable.

def display():
    print('Display function ran.')

decorated_display = decorator_func(display)

decorated_display()

# The above ^ is the same as:

@decorator_func
def display_two():
    string = 'Harry Potter and the Philosopher\'s Stone'
    string = string.split()
    print(str([i for i in string]))

display_two()

# Note: You shouldn't try and print anything in the decorator functions, as it will run those on the first time through. Seems like it would be more wise (or though it has been designed) to do function level logic on the function that takes in the other one.

# However, you can't decorate the same function with the same decorator unless you give the following keywords in the arguments:
# (*args, **kwargs)
# This has to be in both the wrapper function and the return of the original function.
def decorator_func2(original_function):
    def wrapper_func(*args, **kwargs):
        print('derp')
        return original_function(*args, **kwargs)
    return wrapper_func

@decorator_func2
def test_1(msg):
    print(msg)

@decorator_func2
def test_2(msg):
    print(msg)

test_1('Ground control...')
test_2('... to Major Tom')
