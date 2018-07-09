# Attributes: Variables associated with a class (?)
# Methods: A function associated with a class

# Self must be supplied to all methods of the class.
class Employee:
    # The class gives the instance of the object as the first argument.
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return ('{} {}'.format(self.first, self.last))
    # pass    # Pass means to just 'skip that'

# Instance variables and class variables. Instance variables have information that's unique to each instance of the class

# Note that
emp_1 = Employee('Alex', 'Hiller', 'A billion')
emp_2 = Employee('Bruce', 'Willis', 'Too much')

# Interestingly enough, you can assign previously undeclared attributed to the object

print(emp_1.pay)
print(emp_2.pay)

print('Employee two\'s name is: ' + emp_2.fullname())
