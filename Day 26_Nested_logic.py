# Enter your code here. Read input from STDIN. Print output to STDOUT
x,y,z = tuple(map(int,input().split()))
x1,y1,z1 = tuple(map(int,input().split()))
if z <= z1:
    if z == z1 and y > y1:
        print(500*(y-y1))
    elif z == z1 and y == y1 and x > x1:
        print(15*(x-x1))
    else:
        print(0)
else:
    print(10000)
