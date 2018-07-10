# https://www.youtube.com/watch?v=kr0mpwqttM0
# 'First class functions' is a term that helps hyou understand other key python/object oriented programming.
# A 'first class function' is that which can be passed as an argument, assigned to a variable and returned from a function. You're essentially treating the function like a variable.

def square(x):
    return x*x

def cube(x):
    return x*x*x

def _map(func, arg_list):
    result = []
    for i in range(len(arg_list)):
        result.append(func(arg_list[i]))
    return result

# Notice that I'm passing in the function, 'square' but with no parantheses. This is because the parantheses indicates to the compiler to run the function rather than to point to it.
# _list = [2,4,6,8]
# squares = _map(square, _list)
# cubes = _map(cube, _list)
#
# print(squares)
# print(cubes)

# Showing an example of what is not (?) a first class function.
def logger(msg):

    def log_message():
        print('Logging:', msg)

    return log_message # Returning the function within this function?!

log_hi = logger('Hi')
log_hi() # Apparently calling this is called a 'closure', is that because we can't call this again?

log_hi() # Still works!

# An example of how this is useful is a nested function that's purpose is to wrap text:
def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text # Returns a function so that you can make functions for the different tags

para = html_tag('p')
para('Stuff that would go in a paragraph.')
header_one = html_tag('h1')
header_one('A big old title.')
