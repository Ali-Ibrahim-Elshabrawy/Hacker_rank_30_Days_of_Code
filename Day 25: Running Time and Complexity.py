# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def check_prime(num):
    if num == 1:
        return "Not prime"
    sq = int(math.sqrt(num))
    for x in range(2, sq+1):
        if num % x == 0:
            return "Not prime"
    return "Prime"
n = int(input())
for i in range(n):
    print(check_prime(int(input())))
