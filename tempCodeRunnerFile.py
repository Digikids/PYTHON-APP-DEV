my_students = ["Angel", "Jabari", "Jayden", "George", "Risper"]

# def prt_length(x):
#     print(len(x))

# prt_length(data)

def prt_integers(x):
    for i in x:
        if type(i) == int:
            print(i)
        else:
            print(str(i) + " is not an integer")

#prt_integers(data)
#prt_integers(a)
prt_integers(my_students)