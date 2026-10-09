def d1(n):
    if n<0:
        return "fs"
    if n==0 or n==1:
        return 1
    return n * d1(n-1)
num = int(input("zhangsan"))
print(d1(num))
print("hello world")
print("hello world")
print("hello world")
print("hello world")
