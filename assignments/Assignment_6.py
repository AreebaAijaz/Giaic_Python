# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")

student1 = Student("Areeba", 90)
student1.display()
print()




# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1    # Increment count each time object is created

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")

Object1 = Counter()
Object2 = Counter()
Object3 = Counter()

Counter.display_count()
print()




# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:
    def __init__(self, brand):
        self.brand= brand

    def start(self):
        print(f"{self.brand} is starting...")  

Car1 = Car("Corolla")
print("Brand Name:", Car1.brand)  # Accessing public variable
Car1.start()
print()




# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "Faysal Bank"

    def __init__(self, customer):
        self.customer = customer

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name        

    def display(self):
        print(f"Customer: {self.customer}, Bank Name: {Bank.bank_name}")

account1 = Bank("Ali")
account1 = Bank("Sara")

account1.display()
account1.display()

# change the bank name using class method
Bank.change_bank_name("Meezan Bank")

# Show that the change effects all instances 
print("After changing bank name:")
account1.display()
account1.display()
print()




# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

class MathUtils:
    @staticmethod
    def add(a,b):
        return a+b 

result = MathUtils.add(4, 2)
print(f"The sum is: {result}")




# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

class Logger:
    def __init__(self):
        print("Logger object created.")

    def __del__(self):
        print("Logger object deleted.")

log = Logger()

del log
print()




# Create a class Employee with: a public variable name, a protected variable _salary, and a private variable __ssn. Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name       # public
        self._salary = salary     #protected
        self.__ssn = ssn       # private

# create object
emp = Employee("Areeba", 89000, "786-842-0913")

#  access private variable
print("Name:", emp.name)

# access protected variable
print("Salary:", emp._salary)

# access priavte variable
try:
    print("SSN:", emp.__ssn)
except AttributeError as e:
    print("Error accessing SSN:", e)
print()




# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        self.subject = subject
        super().__init__(name) == name

    def display(self):
        print(f"Teacher's name: {self.name} \nSubject: {self.subject}")

teacher_info = Teacher("Areeba", "Mathematics")
teacher_info.display()
print()




# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
rect = Rectangle(5,4)
print(f"The area of Rectangle is {rect.area()}")
print()





# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self, name, breed):
        self.name = name 
        self.breed = breed

    def bark(self):
        print(f"{self.name} the {self.breed} says Woof!")

Dog_info = Dog("Budddy", "dog")
Dog_info.bark()
print()




# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.
class Book:
    total_books = 0

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()
        self.display()

    @classmethod 
    def increment_book_count(cls):
        cls.total_books += 1

    def display(self):
        print(f"Book added: {self.title}")    

Book1 = Book("A Thirsty Crow")
Book2 = Book("Turtle and Rabbit")
print("Total Books:", Book.total_books)
print()





# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class Temperature_converter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 5/9) + 32
    
celsius_temp = 25
fahrenheit_temp = Temperature_converter.celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C is equal to {fahrenheit_temp:.2f}°F")
print()





# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_car(self):
        self.engine.start()

engine = Engine()
car = Car(engine)
car.start_car()
print()





# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name):
        self.name = name 

    def show(self):
        print(f"Employee Name: {self.name}")

class Department:
    def __init__(self, employee):
        self.employee = employee

    def show_employee(self):
        self.employee.show()

emp = Employee("Areeba")
dept = Department(emp)
dept.show_employee()
print()





# Create four classes:   A with a method show(),    B and C that inherit from A and override show(),   D that inherits from both B and C.   Create an object of D and call show() to observe MRO.

class A:
    def show(self):
        print("This is class A.")

class B(A):
    def show(self):
        print("This is class B.")

class C(A):
    def show(self):
        print("This is class C.")

class D(B,C):
    pass

d = D()
d.show()


print(D.__mro__)





# Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().

def log_function_call(func):
    def wrapper():
        print("Function is being called.")
        func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")
    
say_hello()





# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.

def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Areeba")
print(p.greet())





# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        self._price = price  # private attribute (by convention)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Example usage
p = Product(100)
print(p.price)  # Getting the price

p.price = 200  # Setting a new price
print(p.price)

del p.price     # Deleting the price





# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor
    

m = Multiplier(5)

print(callable(m))

result = m(10)
print(result)





# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be atleast 18.")
    
try:
    age = int(input("Enter your age: "))
    check_age(age)
    print("Access granted.")

except InvalidAgeError as e:
    print("Access denied:" , e)





# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            num = self.current
            self.current -= 1
            return num
        
for number in Countdown(10):
    print(number)