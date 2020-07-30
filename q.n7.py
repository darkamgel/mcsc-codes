#q.n 7
#Write a program to calculate the sum of natural n natural numbers 1 + 2 + ⋯ + 𝑛.
#Calculate the sum when 𝑛 = 10
def sum(n):
    if n <= 1:
        return n
    else:
        return n + sum(n-1)
print("The sum is: ", sum(10))