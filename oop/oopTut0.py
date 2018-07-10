# Attributes: Variables associated with a class (?)
# Methods: A function associated with a class

import datetime as dt

# Self must be supplied to all methods of the class.
class Employee:
    raise_amount = 1.05
    num_of_emps = 0 # Initial value

    # The class gives the instance of the object as the first argument.
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emps += 1 # Increment the number of employees each time a new class instance is initialised.

    def fullname(self):
        return ('{} {}'.format(self.first, self.last))

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # Regular methods in a class, take the instance in the class, but if you want to make a method that takes in the class as the first argument you do the following:
    @classmethod
    def set_raise_amt(cls, amount): # The convention is to call a class 'cls' because class is a keyword in python
        cls.raise_amount = amount

    # Example of an alternative constructor. Convention is to start them with a 'from_' to communicate that they are an alternative constructor
    @classmethod
    def from_string(cls, employee_str):
        first, last, pay = (employee_str.split('-'))
        return cls(first, last, pay)

    # nb: The weekday method returns 0 = Monday, through to 6 = Sunday
    @staticmethod
    def is_workday(day):
        if (day.weekday() == 5) or (day.weekday() == 6):
            return False
        return True


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
# print('Class raise_amount is: ' + str(Employee.raise_amount))
# print('Variable 1 raise_amount is: ' + str(emp_1.raise_amount))
# print('Variable 2 raise_amount is: ' + str(emp_2.raise_amount))

# Employee.raise_amount = 1.06
# print('Class raise_amount is: ' + str(Employee.raise_amount))
# print('Variable 1 raise_amount is: ' + str(emp_1.raise_amount))
# print('Variable 2 raise_amount is: ' + str(emp_2.raise_amount))

# So the conclusion is that class attributes kind of act like default values. If you change them, you change the attributes of all those objects of the class, but if you change only one locally then it will store that in its name space

# You can print the namespace of a class instance by typing:
# print(instance.__dict__), e.g.
# print(emp_1.__dict__)
# print(emp_2.__dict__)
# print(Employee.__dict__)

# Video 3: Regular methods, class methods and static methods
# Before class method
# print(Employee.raise_amount)
# Applying class method
# Employee.set_raise_amt(1.10)
# After class method
# print(Employee.raise_amount)

# You can also use an instance to run a class method
# People use class methods as alternative constructors. (A different way to create the object)
# Using this alternative constructor, as such:
# hyphenated_string = 'Tom-Hanks-A Zillion'
# new_emp3 = Employee.from_string(hyphenated_string)
#
# print(str(new_emp3.first) + ' ' + str(new_emp3.last) + ' ' + str(new_emp3.pay))

# Static methods: Don't pass anything automatically. We only inclide them in the class because they have some logical connection to the class.
# E.g. A function that determines whether the day passed in is a weekday or not
# Using datetime module, if you have datetime object you can say: object.weekday()
# The weekday instance method will return 0 = Monday, through the 6 = Sunday
# test_date = dt.datetime(2018, 7, 10)
# print(Employee.is_workday(test_date))
