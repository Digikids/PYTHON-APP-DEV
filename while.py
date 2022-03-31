num = 1

while num < 1000:
    print(num)
    num += 1

m = 1
while m <= 20:
    print(m * "#")
    m += 1

c = True
x = 1
while c == True:
    print("The value of c is True")
    if x > 100:
        c = False
    x += 1

a = 0
while a <= 10:
    if a % 2 == 1:
        print(a)
    a += 1


b = 50
while b <= 60:
    square = b*b
    print("The square of " + str(b) + " is "+ str(square))
    b += 1

m = 20
while m >= 0:
    print(m * "#")
    m -= 1