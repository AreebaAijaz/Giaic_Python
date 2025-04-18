""" ______________ Arithmetic Operators_____________
    ______________+ , - , * , / , // , % , ** __________ """

x = 10
y = 3
print("________ARITHMETIC OPERATORS_________")
print("Addition: x+y =", x+y )
print("Subtraction: x-y =", x-y )
print("Multiplication: x*y =", x*y )
print("Division: x/y =", x/y )
print("Floor Division: x//y =", x//y )
print("Modulus: x%y =", x%y )
print("Exponential: x**y =", x**y )
print()

""" ______________ Assignment Operators_____________
    ______________ = , += , -= , *= , /= , //= __________ """

print("________ASSIGNMENT OPERATORS_________")

print("Assignment: x=     " , x)

x+=7
print("Addition Assignment: x+=7     ", x)

x-=7
print("Subtraction Assignment: x-=7     ", x)

x*=7
print("Multilpication Assignment: x*=7     ", x)

x/=7
print("Division Assignment: x/=7     ", x)

x//=7
print("Foor Division Assignment: x//=7     ", x)
print()


""" ______________ Comparison Operators_____________
    ______________ == , != , >= , <= __________ """
x= 10
y= 3
print("________cOMPARISON OPERATORS_________")
print("x==y:  ", x==y)
print("x!=y:   ", x!=y)
print("x>y:  ", x>y)
print("x<y:  ", x<y)
print("x>=y:  ", x>=y)
print("x<=y:  ", x<=y)
print()


""" ______________Logical Operators_____________
    ______________ and , or , not __________ """
print("________LOGICAL OPERATORS_________")

print("x==10 and y==2   ", x==10 and y==2)
print("x==10 or y==2   ", x==10 or y==2)
print("not x   ", not x)
print()


""" ______________Identity Operators_____________
    ______________ is , is not  __________ """
a:list = [1,2,3]
b:list = [1,2,3]
print("________IDENTITY OPERATORS_________")
print("a is b:   ", a is b)
print("a is not b:   ", a is not b)
print("a == b:   ", a == b)
print("a != b:   ", a != b)
print()


""" ______________Membership Operators_____________
    ______________ in , not in  __________ """

print("________MEMBERSHIP OPERATORS_________")
my_alphabets:list = ['a' , 'f' , 'm' , 's']
print("'a' in my_alphabets?   ", 'a' in my_alphabets)
print("'k' in my_alphabets?   ", 'k' in my_alphabets)
print("'z' not in my_alphabets?   ", 'z' not in my_alphabets)
print()

""" ______________ Bitwise NOT Operator(~)_____________ """
x=10
y= ~x
z= 5
print("________BITWISE OPERATORS_________")
print("X=", x)
print("y=", y)
