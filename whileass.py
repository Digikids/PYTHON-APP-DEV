import functions as fn
import math

i = 10
x = []

while i > 1:
    x.append(i*i)
    i -= 1

y = []

for i in x:
    y.append(math.sqrt(i))

print(y)

fn.prt_integers(y)

x = range(10, 310, 10)
z = []
for n in x:
    z.append(n)

print(z)


t = 105
z = []
while t > 0:
    z.append(t)
    t -= 7

print(z)