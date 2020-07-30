#q.n 5
#ax^2+bx+c=0 ,
from math import *
def nature(a,b,c):
    discrimant=b**2-4*a*c
    if(discrimant>0):
        root1 =(-b+sqrt(discrimant))/(2*a)
        root2 = (-b + sqrt(discrimant)) / (2 * a)
        print("the nature is real  and unequal . And the root are ",root1,root2)
    elif(discrimant==0):
        root1 = root2 = -b / (2 * a)
        print("the nature is equal and real . And the root are ",root1)
    else:
        realPart = -b / (2 * a)
        imagPart = sqrt(-discrimant) / (2 * a)

        print("the nature is imaginary . And the roots are",realPart,imagPart)
nature(2,3,4)
nature(2,33,4)
nature(2,4,2)

