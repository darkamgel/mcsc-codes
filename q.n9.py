#q.n 9
#Write a program to find the smallest integer n such that 3𝑛 ≥ 2000

n=0
while 1:
    if (3**n>=2000):
        break
    n+=1

print("the number is ",n)
