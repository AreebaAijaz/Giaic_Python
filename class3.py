"_______Control Flow________"
name = input("Enter Your Name:\t")
if len(name) <= 5:
    print(f"Your name contains {len(name)} alphabets.")
elif len(name) <= 10:
    print(f"your name contains {len(name)} alphabets and that's perfect.")
else:
    print(f"Your name is too long!")


"_______Loops________"
A = [3,6,9]
i = 1
for var1 in A:
    print(f"The value of 'A' in iteration {i} is {var1}")
    i += 1

"_______Nested Loops________"
for i in range(1,4):
    for j in range(1,4):
        print(i,j)
    print("Now we are outside the inner loop.")
print("Now we are outside the outer loop.")    
print()

"_______Lists________"
my_list = ["apple" , "mango" , "banana" , "pineapple" , "cherry"]
print("my_list:   ", my_list)
my_list.append("guava")
print("my list after appending guava:   " , my_list)
my_list.pop()
print("my list after poping:   ", my_list)
my_list.insert(2, "grapes")
print("my list after inserting grapes:   ", my_list )
my_list = my_list.__add__(["dates" , "strawberry"])
print("my list after a list:   ", my_list )
print()

"_______Tuples________"
# creating a tuple
my_tuple = (1,2,3,4,5)
print("ORIGINAL TUPLE:" , my_tuple)

# accessing elements
print("First Element:" , my_tuple[0])
print("Last Element:" , my_tuple[-1])

# slicing the tuple
print("Sliced tuple fom 2nd to 4th element:", my_tuple[1:4] )

# concatenation 
new_tuple = my_tuple + (6,7)
print("Concatenated Tuple:" , new_tuple)

# repetition
repeated_tuple = my_tuple * 2
print("Repeated Tuple:" , repeated_tuple)

# membership test
print("Is 3 in tuple?" , 3 in my_tuple)
print("Is 9 in tuple?" , 9 in my_tuple)

# length of tuple
print("Length ofTuple:" , len(my_tuple))

# indexing
print("Index of element 5 is:" , my_tuple.index(5))

# counting element
print("Count of an element 2:" , repeated_tuple.count(2))


"_______Dictionary________"
my_dict = {'a':1 , 'b':2 , 'c':3}
print("Variables stored in my dictionary:" , my_dict)

# accessing elements
print("value for key 'a'=" , my_dict['a'])
print("value for key 'b'=" , my_dict['b'])

# adding and updating element
my_dict['d'] = 4
print("Dictionary after adding key'd':" , my_dict)
my_dict['a'] = 10
print("Dictionary after updating key'a':" , my_dict)

# removing elements
del my_dict['b']
print("Dictionary after removing key'b':" , my_dict)
removed_value = my_dict.pop('c')
print("Removed value of 'c':" , removed_value)
print("Dictionary after removing 'c':" , my_dict)
print()


"_______Sets_______"
setA = {1,2,3,4,5,6}
setB = {2,4,6,8}
# calculating union
union = setA.union(setB)
print("Union of setA and setB:" , union)   # Union of setA and setB: {1, 2, 3, 4, 5, 6, 8}

# calcuating intersection
intersection = setA.intersection(setB)
print("Intersction of setA and setB:" , intersection)    # Intersction of setA and setB: {2, 4, 6}

# calculating difference
difference = setA.difference(setB)
print("Difference of setA and setB:" , difference)     # Difference of setA and setB: {1, 3, 5}

# symmetric difference
symmetric_difference = setA.symmetric_difference(setB)
print("Symmetric difference of setA and setB:" , symmetric_difference)   #Symmetric difference of setA and setB: {1, 3, 5, 8}


