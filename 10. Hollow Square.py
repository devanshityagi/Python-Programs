n=int(input("Enter no. of rows/columns: "))
for i in range(n):
    if (i==0 or i==n-1):
        print("*" * n)
    else:
        print("*" + " " * (n-2) + "*")
