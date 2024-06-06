##f = open('27-99a.txt')
##n = int(f.readline())
##a = [int(i) for i in f]
##res=[]
##for i in range(n):
##    st = 0
##    for j in range(n):
##        st += a[j]*min(abs(j-i), n - abs(j-i))
##    res.append([st, i])
##print(min(res))

##f = open('27-10a.txt')
##n = int(f.readline())
##summ=0
##razn=[]
##for s in f:
##    troyka = list(map(int, s.split()))
##    troyka.sort()
##    summ += max(troyka)
##    if (troyka[2]-troyka[1])%4!=0:
##        razn.append(troyka[2]-troyka[1])
##    if (troyka[2]-troyka[0])%4!=0:
##        razn.append(troyka[2]-troyka[0])
##if summ%4==0:
##    summ -= min(razn)
##print(summ)

##f = open('27-a.txt')
##n = int(f.readline())
##summ = 0
##razn = []
##for s in f:
##    a, b = map(int, s.split())
##    summ += max(a, b)
##    if abs(a - b)%3!=0:
##        razn.append(abs(a-b))
##if summ%3==0:
##    summ -= min(razn)
##print(summ)




##f = open('27-178a.txt')
##n = int(f.readline())
##a = [int(i) for i in f]*2
##p = [0]
##for i in a:
##    p.append(p[-1] + i)
##r=0
##for i in range(n+1):
##    for j in range(i+1, i+n+1):
##        if p[j] - p[i] > r:
##            r = p[j] - p[i]
##print(r)
        

        


##f = open('27-169a.txt')
##n,k = map(int, f.readline().split())
##a = [int(i) for i in f.readlines()]
##cnt=0
##for i in range(n):
##    for j in range(i+1, n):
##        if (a[i]+a[j])>=k:
##            cnt+=1
##print(cnt)

##f = open('27-165a.txt')
##n, k = map(int, f.readline().split())
##mn = 10**20
##a = [int(i) for i in f.readlines()]
##for i in range(n):
##    for j in range(i+k, n):
##        for p in range(j+k, n):
##            if (a[i]+a[j]+a[p])<mn:
##                mn = min(mn, (a[i]+a[j]+a[p]))
##print(mn)

##f= open('27-75a.txt')
##n = int(f.readline())
##a = [int(i) for i in f.readlines()]
##mx=0
##ans=[]
##for i in range(n):
##    s=0
##    for j in range(i,n):
##        s+=a[j]
####        if (s%43==0) and (mx<s):
####            mx = s
##        if s==1806387:
##            print(j-i+1)


##f = open('27-14a.txt')
##n = int(f.readline())
##a = sorted([int(i) for i in f.readlines()])
##k=0
##for i in range(n-1):
##    for j in range(i+1, n):
##        if (i>=0) and (j<=n) and (i<j) and ((a[i]+a[j])%12==0):
##            k+=1
##        j+=1
##print(k)

##f = open('27-9a.txt')
##n = int(f.readline())
##a = [int(i) for i in f.readlines()]
##mn=10**20
##for i in range(n-6):
##    for j in range(i+6, n):
##        if (a[i]*a[j])%2!=0:
##            mn = min(mn, (a[i]*a[j]))
##print(mn)

##f = open('27-7a.txt')
##n = int(f.readline())
##a = [int(i) for i in f.readlines()]
##r=1
##for i in range(n-1):
##    for j in range(i+1, n):
##        if (a[i]*a[j])%7==0 and (a[i]*a[j])%49!=0:
##            r = max(r, (a[i]*a[j]))
##print(r)




##f = open('27-4a.txt')
##n = int(f.readline())
##summ=0
##razn=[]
##for s in f:
##    a = [int(x) for x in s.split()]
##    summ += max(a)
##
##    razn.append(abs(a[0]-a[1]))
##if summ%5!=0:
##    summ -= min(razn) 
##print(summ)
