#q.n 4
from numpy import *
def answer():
    g=9.8
    h0=10
    t=arange(10,0,-0.5)
    y=h0-0.5*g*t**2
    print("the value of y is:",y)
    print("----------------------------------------------------------------------------------------------")
    print("----------------------------------------------------------------------------------------------")
 #for time
    num=sqrt(2*(h0-y))
    dem=g
    time=(num/dem)
    print("the sequence of time is :",time)
    print("----------------------------------------------------------------------------------------------")
    print("----------------------------------------------------------------------------------------------")
#for average velocity
    avgvelocity=(y/t)
    print("the values of avg velocity is  ",avgvelocity)
answer()


