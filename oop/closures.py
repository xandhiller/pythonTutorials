# def outer_func():
#     message = 'Hi'
#
#     def inner_func():
#         print(message)
#
#     return inner_func
#
# my_func = outer_func()
#
# print(my_func)
# # My func has been assigned inner_func, as you can see if you run the line below.
# print(my_func.__name__)

# Going to tweak the function, so recopying it.
def outer_func(msg):
    def inner_func():
        print(msg)
    return inner_func

gday_func = outer_func('G\'day!')
howsit_func = outer_func('Howsit?!')

gday_func()
howsit_func()
# Each of these functions have saved what was passed into them, so even though we've used the same function to create them both, they can each run the logic with the variables they were passed.
