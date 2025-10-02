n=int(input("Enter no. of rows of inverted pyramid: "))
for i in range(n):
    print((" " * i) + ("*" * (2*(n-i)-1)))
