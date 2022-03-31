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

