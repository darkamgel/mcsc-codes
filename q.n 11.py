#q.n 11
from numpy import *
from  matplotlib.pyplot import *

x= linspace(-2*pi,2*pi,100)
y1=sin(x)
y2=cos(x)

plot(x,y1,'r')
plot(x,y2,'b')

xlabel('x-axis')
ylabel('y-axis')
title('solution of question 11')
legend(['sinx','cosx'])
show()