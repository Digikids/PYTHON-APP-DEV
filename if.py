num = 16

if num < 5:
    print(num, "is less than 5")
elif num < 10:
    print(num, "is less than 10")
elif num < 15:
    print(num, "is less than 15")
else:
    print(num, "is neither less than 5, 10 and 15")

print("This statement will always execute")

my_name = 0

if type(my_name) == str:
    print(my_name, "is a string")
elif type(my_name) is int:
    print(my_name, "is an integer")
elif type(my_name) == float:
    print(my_name, "is a float")
else:
    print(my_name, "is a boolean value")