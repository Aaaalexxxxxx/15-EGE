for A in range(1,1000):
    s=1
    for x in range(1,500):
        if ((x%A==0) or ((70<=x<=80) <= (x%18!=0)))==0:
            s=0
    if s==1:
        print(A)


##for A in range(10000):
##    s=1
##    for x in range(1, 1000):
##        for y in range(1, 1000):
##            if (((x**2 - 11*x + 28)>0) or ((y**2 - 9*y +14)>0) or ((x**2 + y**2)>A))==0:
##                s=0
##    if s==1:
##        print(A)

        
##from itertools import *
##def f(x):
##    P = 25<=x<=50
##    Q = 40<=x<=75
##    A = a1<=x<=a2
##    return Q <= ((P==Q) or ((not P) <= A))
##Ox = [i/4 for i in range(25*4,75*4+1)]
##m=[]
##for a1,a2 in combinations(Ox,2):
##    if all(f(x)==1 for x in Ox):
##        m.append(a2-a1)
##print(min(m)) #24.75 --> 25


##p = {3,6,9,12}
##q = {1,2,3,4,5,6}
##a = set()
##def f(x):
##    return (not((x not in a) and (x in p))) or (x not in q)
##for x in range(1,1000):
##    if f(x)==0:
##        a.add(x)
##print(a)


##p = {2,4,6,8,10,12,14,16,18,20}
##q = {5,10,15,20,25,30,35,40,45,50}
##a = set(range(1,1000))
##def f(x):
##    return ((x in a) <= (x in p)) and ((x in q) <= (x not in a))
##for x in range(1,1000):
##    if f(x)==0:
##        a.remove(x)
##print(a)


##for A in range(1, 1_000):
##    s=1
##    for x in range(1, 500):
##        if ( (x&87==0) <= ((x&31!=0) <= (x&A!=0)) )==0:
##            s=0
##    if s==1:
##        print(A)
##        break
