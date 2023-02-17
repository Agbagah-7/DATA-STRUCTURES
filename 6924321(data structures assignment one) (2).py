# Assignment one data structures.
l=12 # span of beam
w=10 # load intensity
#Qa. Bending moment(M) and shear force(V) 
x=0
M=(w*(-6*x**2+6*l*x-l**2))/12
V=w*(l/2-x)
print('Q(a.1).Bending moment at x=0 is') 
print(M)
print(V) 
a=l
M=(w*(-6*a**2+6*l*x-l**2))/12
V=w*(l/2-a)
print('Q(a.2).Bending moment when x=l is')
print(M)
print(V)
#Qb.
# x**2-l*x+l**2/6  is the expression when moment is zero.
# obtaining the roots of the quadratic equation, let D = discriminant.
b=l
f=1
c=1/6
D=b**2-4*f*c
# using the almighty quadratic formular
import numpy as np
root_1a=(-b+np.sqrt(D))/2*f
root_2a=(-b-np.sqrt(D))/2*f
print('Qb.Points of contra-flexure=')
print(root_1a)
print(root_2a)  
#Qc. let X=K when shear force v=0
x=l/2
print('Q(c).Point on the beam where shear force is zero=') 
print(l/2)
#Qd. 10mm=0.01m
x=np.arange(0,12,0.01)  
# let M=Z 
z=(w*(-6*x**2+6*l*x-l**2))/12 
print('Qd.Bending moment at each step along the span=')
print(z)
#Qe
#let V=S 
S=w*(l/2-x)
print('Qe.Shear force at each step along the span=')
print(S)
#Qf
"""let the absolute value of the bending moment array be Ab 
also let the minimum absolute value be mi"""
"""For minimum bending moment, use the expression x**2-lx+(l**2/6)+(2*mi)/w=0"""
# let Q= discriminant
Ab=abs(z)
mi=min(Ab)
b=-l
a=1
c=(l**2/6)+(2*mi)/w
Q=b**2-4*a*c
root_1b=(-b+np.sqrt(Q))/2*a
root_2b=(-b-np.sqrt(Q))/2*a
print()
print('Q(f).The points of minimum absolute bending moment array values are {0} and {1}'.format(root_1b,root_2b))
#Qg
"""let the relative errors be r1 and r2"""
r1=((root_1a-root_2a)/root_1a*100)
r2=((root_1b-root_2b)/root_1b*100)
print()
print('Q(g).The relative errors between estimated points of contra-flexure are {0}% and {1}%'.format(r1,r2))
#Qh
max_M=max(z) #for maximum bending moment.
"""When the bending moment is max_M,we get an expression x**2-lx+(l**2/6)+(2*max_M)/w=0"""
a=1
b=-l
c=(l**2/6)+(2*max_M)/w
J=b**2-4*a*c # where J is the discriminant.
root_3a=(-b+np.sqrt(J))/2*a
root_3b=(-b-np.sqrt(J))/2*a
print()
print('Q(h.1).The points at which maximum bending moment occur are {0} and {1}'.format(root_3a,root_3b))
min_M=min(z) #for the minimum bending moment
"""when the bending moment is min_M, we get an equation x**2-lx+(l**2/6)+(2*min_M)/w"""
a=1
b=-l
c=(l**2/6)+(2*min_M)/w
P=b**2-4*a*c #let P be the discriminant.
root_4a=(-b+np.sqrt(P))/2*a
root_4b=(-b-np.sqrt(P))/2*a
print()
print('Q(h.2).The points at which the minimum bending moment occur are {0} and {1}'.format(root_4a,root_4b))
# Github account  link(https://github.com/users/Agbagah-7)
                                                                                                    
