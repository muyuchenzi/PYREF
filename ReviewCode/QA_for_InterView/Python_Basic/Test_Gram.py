from sympy import im


import sys
f=[x for x in range(1,11)]
f2=[x+str(y) for x in "abcde" for y in range(1,8)]
f3=[x**2 for x in range(1000)]
f4=[]
for i in range(1000):
    f4.append(i)

print(sys.getsizeof(f3))
print(sys.getsizeof(f4))
f5=(x**2 for x in range(1000))
print(sys.getsizeof(f5))


def fib(n):
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
        yield a
def main():
    for val in fib(20):
        print(val)
main()

pass
