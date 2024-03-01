from math import ceil, floor

I1, I2, B = input().split(" ")

def toBase10(s: str, b)->int:
    res= 0
    m = 1
    for d in reversed(s):
        res+=(int(d)*m)
        m*=b
    return res 

def toBase(n:int, b:int)->str:
    res = ""
    while n != 0:
        res = str(n % b) + res
        n=n//b
    return res

def add(x,y):
    i1 = len(x) - 1
    i2 = len(y) - 1
    carry = 0
    res = ''
    while i1 >=0 or i2>=0:
        temp = carry
        if i1 >= 0: 
            temp += int(x[i1])
            i1 -=1
        if i2 >=0:
            temp += int(y[i2])
            i2-=1
        res = str(temp % int(B)) + res
        carry = temp // int(B)
    if carry > 0:
        res = '1' +res
    return res
def karatsuba(x,y):
    #base case
    if x < 10 and y < 10: # in other words, if x and y are single digits
        return x*y

    n = max(len(str(x)), len(str(y)))
    m = ceil(n/2)   #Cast n into a float because n might lie outside the representable range of integers.

    x_H  = x // 10**m
    x_L = x % (10**m)

    y_H = y // 10**m
    y_L = y % (10**m)

    #recursive steps
    a = karatsuba(x_H,y_H)
    d = karatsuba(x_L,y_L)
    e = karatsuba(x_H + x_L, y_H + y_L) - a - d

    return int(a*(10**(m*2)) + e*(10**m) + d)

def divide(x,y): 
    return x // y

sum=add(I1,I2)
q = divide(toBase10(I1,int(B)),toBase10(I2,int(B)))
mul = karatsuba(toBase10(I1,int(B)),toBase10(I2,int(B)))
print(sum,toBase(mul,int(B)),toBase(q,int(B)))
