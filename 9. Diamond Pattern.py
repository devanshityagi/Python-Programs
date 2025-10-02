n=int(input("Enter no. of rows: "))
for i in range(n):
    a=abs(n//2 - i)
    b=n-2*a
    print((" " * a) + ("*" * b))
