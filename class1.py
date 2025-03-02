# datatypes in python 

# 1. int
my_age:int = 37
print("My age is:" , my_age)

# 2. float
my_height:float = 5.1
print(f"${my_height} is my height")

# 3. string
my_name: str = "Areeba Aijaz"
print("My name is ", my_name)

# 4. boolean
is_student:bool = True
print("Am I a student?" , is_student)

# 5. list
fruits_name:list = ["apple", "mango", "banana"]
print(fruits_name)
fruits_name.append("cherry")
fruits_name.remove("mango")
print(fruits_name)
# membership check
print("apple" in fruits_name)
print("Is mango in fruits?", "mango" in fruits_name)

# 6. tuple
my_tuple:tuple = (4, 5)
print(my_tuple)
new_tuple = my_tuple + (6, 7)
print(new_tuple)

# 7. dictionary
my_dict:dict = {
    "name": "Areeba",
    "age": 18,
    "is_student": True
}
my_dict["passion"] = "Programming"
print(my_dict)
print(my_dict["name"])

# 8. array
import array as arr
array_1 = arr.array('i', [1, 2, 3, 4, 5])
print(array_1)

# 8. set
set_A:set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set_B:set = {2, 4, 6, 8, 10, 11}
print(set_A.intersection(set_B))
print(set_A.symmetric_difference(set_B))

# 9. None
empty_variable:None = None
print(empty_variable)

# 10. bytes
byte_data:bytes = b"This is a byte."
print(byte_data)
