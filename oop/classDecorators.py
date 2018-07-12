class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    # This dunder call method acts as the equivalent of a wrapper function.
    def __call__(self, *args, **kwargs):
        print('Call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)

@decorator_class
def test_1(msg):
    print(msg)

@decorator_class
def test_2(msg):
    print(msg)

test_1('Ground control...')
test_2('... to Major Tom')

# Why an argument to the class
# What do *args and **kwargs really mean
# What are the benefits of using a class versus nested functions for decorating?
# Besides mathematical objects, what are some uses of classes?
