# Attributes: Variables associated with a class (?)

# Methods: A function associated with a class

class Employee:
    # The class gives the instance of the object as the first argument.
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay


    # pass    # Pass means to just 'skip that'

# Instance variables and class variables. Instance variables have information that's unique to each instance of the class

emp_1 = Employee()
emp_2 = Employee()

# Interestingly enough, you can assign previously undeclared attributed to the object

emp_1.email = 'test@email.com'
emp_2.email = 'anotherTest@email.com'
print(emp_1.email)
print(emp_2.email)
