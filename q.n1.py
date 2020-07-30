#question number 1
def height(t):
    g = 9.8
    h0 = 1.2
    v0 = 5.4
    v = v0 - g * t
    print("the value of velocity is%5.3f" %v)
    h=h0+v0*t-(1/2)*g*t**2
    print("the height is %5.3f"%h)

#when time is 0.5 seconds
height(0.5)
#when time is 2 seonds
height(2)