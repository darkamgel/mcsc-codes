##using for loop
x=int(input("enter the number whose factorial to be known ="))
if(x==0):
    print("the factorial is 0")
else:
    def fact(n):
        f=1
        for i in range(1,n+1):
            f=f*i
        return f
    result = fact(x)
    print(result)
###while loop
print("for while loop")
num=int(input("enter a number whose factorial you want to know:"))
n1=1
fact=1
if(num==0):
    print("the fact is 0")
else:
    while(n1<=num):
        fact=fact*n1
        n1+=1
    print(fact)





