def hello(x):
    print("Hello " + x)

hello("Steve")
hello("Jayden")

def multiply(x,y):
    print(x*y)

multiply(9,8)
multiply(100, 6)

def check_datatype(my_name):
    if type(my_name) == str:
        print(my_name, "is a string")
    elif type(my_name) is int:
        print(my_name, "is an integer")
    elif type(my_name) == float:
        print(my_name, "is a float")
    else:
        print(my_name, "is a boolean value")

check_datatype(True)
check_datatype(5.6)

data = [2,"Angel", 5, 6, 7.9, "Jabari",
"Jayden",2.3, True, "List", False, "George", "Risper"]
a =[1,2,3,4,5,6,7,8,9,10]
my_students = ["Angel", "Jabari", "Jayden", "George", "Risper"]

def prt_length(x):
    print(len(x))

prt_length(data)

def prt_integers(x):
    for i in x:
        if type(i) == int:
            print(i)
        else:
            print(str(i) + " is not an integer")

prt_integers(data)
prt_integers(a)
prt_integers(my_students)