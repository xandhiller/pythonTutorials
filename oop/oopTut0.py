# Attributes: Variables associated with a class (?)
# Methods: A function associated with a class

# Self must be supplied to all methods of the class.
class Employee:
    raise_amount = 1.05

    # The class gives the instance of the object as the first argument.
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return ('{} {}'.format(self.first, self.last))

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # pass    # Pass means to just 'skip that'

# Instance variables and class variables. Instance variables have information that's unique to each instance of the class

# Note that
emp_1 = Employee('Alex', 'Hiller', 'A billion')
emp_2 = Employee('Bruce', 'Willis', 'Too much')

# Interestingly enough, you can assign previously undeclared attributed to the object

# print(emp_1.pay)
# print(emp_2.pay)

# print('Employee two\'s name is: ' + emp_2.fullname())

# Something interesting worth noting about class and instance attributes:

emp_1.raise_amount = 1.07
print('Class raise_amount is: ' + str(Employee.raise_amount))
print('Variable 1 raise_amount is: ' + str(emp_1.raise_amount))
print('Variable 2 raise_amount is: ' + str(emp_2.raise_amount))

Employee.raise_amount = 1.06
print('Class raise_amount is: ' + str(Employee.raise_amount))
print('Variable 1 raise_amount is: ' + str(emp_1.raise_amount))
print('Variable 2 raise_amount is: ' + str(emp_2.raise_amount))
