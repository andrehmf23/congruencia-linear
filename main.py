m = 9
a = 7
c = 4
x = 3

for i in range(20):
    x = (a * x + c) % m
    print(x)