''' Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

''' Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())
process = True
sad = True
while process == True:
    for x in range(-10,10):
        for y in range(-10,10):
            if(a*x + b*y != c) and (d*x + e*y != f):
                sad = True
                continue
            if(a*x + b*y == c) and (d*x + e*y == f):
                print(x,y)
                process = False
                break
