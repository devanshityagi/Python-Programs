n=int(input("Enter no. of rows in pyramid: "))
for i in range(n):
    print((" " * (n-i-1)) + ("*" * (2*i+1)))