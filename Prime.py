#1
def getBalancedPrime(startLimit,endLimit,balancedMode):
    l1=[]
    p,r,c=startLimit,endLimit,balancedMode
    if p==1:
        p=2
    l=[]
    for a in range(p,r+1):
        k=0     
        for i in range(2,int(a/2)+1): 
            if(a%i==0):
                k=k+1     
                break
        if(k<=0):         
            l.append(a)
    for i in range(c,int(len(l)-1),1):
        m=l[i]
        p=i-1
        q=i+1
        sum=0
        z=c
        while(p>=0 and z>0 and q<len(l)):
            sum=sum+l[p]+l[q]
            q+=1
            p-=1
            z=z-1
        x=q-p-2
        x=sum/x
        if(x-int(x)==0):
          if(x==m):
            l1.append(m)
    return l1
#2
def circular(x):
    u=list(map(int, str(x)))
    f=0
    for i in range(len(u)-1):
        a=u[0]
        u.remove(u[0])
        u.append(a)
        sum=0
        k=0
        j=len(u)-1
        while(j>=0):
            sum=sum+u[k]*(10**j)
            j-=1
            k+=1
        a=sum
        for i in range(2,int(a/2)+1): 
            if(a%i==0):
                f=1    
                break
        if f==1:
            break
    if f==0:
        return(x)
def getCircularPrime(startLimit,endLimit):
    l1=[]
    p,r=startLimit,endLimit
    if p==1:
        p=2
    for a in range(p,r+1):
        k=0     
        for i in range(2,int(a/2)+1): 
            if(a%i==0):
                k=k+1     
                break
        if(k<=0):         
            c1=circular(a)
            l1.append(c1)
    l1=list(filter(None,l1))
    return(l1)
#3
def getCousinPrime(startLimit,endLimit):
    l1=[]
    p,r=startLimit,endLimit
    if p==1:
        p=2
    x=''
    y=''
    #this is exception so we have to print explicitly
    q=[]
    if p<4 and r>6:
        q.append(3)
        q.append(7)
        l1.append(q)
    for a in range(p,r+1): 
        k=0     
        q=[]
        for i in range(2,int(a/2)+1): 
            if(a%i==0):
                k=k+1     
                break
        if(k<=0):  
            if(x==''):
                x=int(a)
                continue
            if(y==''):
                y=int(a)
                if((y-x)==4):
                    q.append(x)
                    q.append(y)
                    l1.append(q)
            else:
                x=y
                y=a
                if((y-x)==4):
                    q.append(x)
                    q.append(y)
                    l1.append(q)
    return(l1)
#4
def getDoubleMersennePrime(startLimit,endLimit):
    l1=[]
    p,r=startLimit,endLimit
    import  math
    if p==1:
        p=2
    for a in range(p,r+1):
        k=0     
        for i in range(2,int(a/2)+1): 
            if(a%i==0):
                k=k+1     
                break
        if(k<=0):  
            a+=1
            x=math.log2(a)
            z=x-int(x)
            if z==0:
                x+=1
                x=math.log2(x)
                z=x-int(x)
                if z==0:
                    l1.append(a-1)
    return(l1)
#5
def c_fact(n):
    i=2
    if n==0:
        return 0
    while int(n)>1:
        n=n/i
        i+=1
    z=n-int(n)
    if(z==0):
        return 1
    return 0
def getFactorialPrime(startLimit,endLimit):
    l1=[]
    p,r=startLimit,endLimit
    if p==1:
        p=2
    for a in range(p,r+1):
        k=0     
        for i in range(2,int(a/2)+1): 
            if(a%i==0):
                k=k+1     
                break
        if(k<=0):  
            x=a-1
            y=a+1
            x=c_fact(x)
            if x==1:
                l1.append(a)
            else:
                if 1==(c_fact(y)):
                    l1.append(a)
    return(l1)
#6
def getGoodPrime(startLimit,endLimit):
    l1=[]
    s,r=startLimit,endLimit
    q=[]
    b=0
    p=2
    for a in range(p,r+1):
        k=0     
        for i in range(2,int(a/2)+1): 
            if(a%i==0):
                k=k+1     
                break
        if(k<=0):  
            q.append(a)
            b=b+1
    a=r+1
    c=b
    while(b>0):
        k=0     
        for i in range(2,int(a/2)+1): 
            if(a%i==0):
                k=k+1     
                break
        if(k<=0):  
            q.append(a)
            b=b-1
        a=a+1
    while(c>0):
        if b>0:
            x=b
            f=0
            while(x>0):
                if(q[b]**2)<(q[b-x]*q[b+x]):
                    f=1
                x=x-1
            if f==0:
                if q[b]>s:
                    l1.append(q[b])
        b=b+1
        c=c-1
    return(l1)
#7
def getMersennePrime(startLimit,endLimit):
    l1=[]
    p,r=startLimit,endLimit
    import  math
    if p==1:
        p=2
    for a in range(p,r+1):
        k=0     
        for i in range(2,int(a/2)+1): 
            if(a%i==0):
                k=k+1     
                break
        if(k<=0):  
            a+=1
            x=math.log2(a)
            x=x-int(x)
            if x==0:
                l1.append(a-1)
    return(l1)
#8
def getPalindromicPrime(startLimit,endLimit):
    l1=[]
    x,y=startLimit,endLimit
    if x==1:
        x=2
    for a in range(x,y+1):
        k=0     
        for i in range(2,int(a/2)+1): 
            if(a%i==0):
                k=k+1     
                break
        if(k<=0):         
            sum=0
            num=a
            q=0
            p=[]
            while(num>0):
                rem=num%10
                p.append(rem)
                num=int(num/10)
                q+=1
                m=0
                while(q>0):
                    sum=sum+p[m]*(10**q)
                    m+=1
                    q-=1
                    sum/=10
                    if(a==sum):
                        l1.append(a)
    return(l1)
#9,,check!!!!!!!
def permutable(n):
    u=list(map(int, str(n)))
    f=0
    import itertools
    p1=list(itertools.permutations(u))
    for i in range(1,len(p1)):
        j=len(p1[0])-1
        sum=0
        k=0
        while(j>=0):
            sum=sum+p1[i][k]*(10**j)
            j-=1
            k+=1
        a=sum
        for i in range(2,int(a/2)+1): 
            if(a%i==0):
                f=1    
                break
        if f==1:
            break
    if f==0:
        return(n)
def getPermutablePrime(startLimit,endLimit):
    l1=[]
    p,r=startLimit,endLimit
    if p==1:
        p=2
    for a in range(p,r+1):
        k=0     
        for i in range(2,int(a/2)+1): 
            if(a%i==0):
                k=k+1     
                break
        if(k<=0):         
            l1.append(permutable(a))
    
    return([i for i in l1 if i])
#10
def check_Primorial(a):
    if(a<8):
        return 1
    p=a/2
    
    if(p!=int(p)):
        return 0
    while(p>0):
        for i in range(3,int(a/2)+1):
            f=0
            for j in range(2,i):
                if(i%j==0):
                    f=1
                    break
            if(f==0):
                
                p=p/i
                if(p!=int(p)):
                    p=0
                    break
                if(p==1):
                    return 1
    return 0      
def getPrimorialPrime(startLimit,endLimit):
    l1=[]
    p,q=startLimit,endLimit
    if(p==1):
        p=2
    for i in range(p,q):
        if(check_Prime(i)):
            x=0
            x=check_Primorial(i-1)
            if x==1:
                l1.append(i)
            else:
               x=check_Primorial(i+1)
               if x==1:
                   l1.append(i)
    return(l1)
#11
#p=int(input("Base"))
#r=int(input("How many Pseudoprime "))
def isComposite(x):
    f=0
    for i in range(2,(x//2)+1):
        if x%i==0:
            f=1
            break
    if f==1:
        return True
    else:
        return False                 
def getFermatPseudoPrime(startLimit,endLimit,baseNumber):
    l1=[]
    p=baseNumber
    q,r=startLimit,endLimit
    if p<2:
        print("enter balanced mode greater than one")
        return l1
    if q==1:
        q=2
    for i in range(q,r):
        x=i
        a=(pow(p,(x-1))-1)%x
        if a==0:
            if(isComposite(x)):
                l1.append(x)
    return(l1)
#12
def getPythagoreanPrime(startLimit,endLimit):
    l1=[]
    p,r=startLimit,endLimit
    if p==1:
        p=2
    for a in range(p,r+1):
        k=0     
        for i in range(2,int(a/2)+1): 
            if(a%i==0):
                k=k+1     
                break
        if(k<=0):         
            p=a
            p-=1
            p/=4
            if(p-int(p)==0):
                l1.append(a)
    return(l1)
#13
def getReversiblePrime(startLimit,endLimit):
    l1=[]
    x,y=startLimit,endLimit
    if x<12:
        x=12
    for a in range(x,y+1):
        k=0  
        sum=0
        for i in range(2,int(a/2)+1): 
            if(a%i==0):
                k=k+1     
                break
        if(k<=0):         
            
            num=a
            q=0
            p=[]
            while(num>0):
                rem=num%10
                p.append(rem)
                num=int(num/10)
                q+=1
                m=0
            while(q>0):
                sum=sum+p[m]*(10**q)
                m+=1
                q-=1
            sum=int(sum/10)
            k=0     
        for i in range(2,int(sum/2)+1): 
            if(sum%i==0):
                k=k+1     
                break
        if(k<=0):
            l1.append(a)
    return(l1)
#14
def getSemiPrime(startLimit,endLimit):
    p,r=startLimit,endLimit
    l1=[]
    for a in range(p,r+1):
        j=a
        n=a
        x=[]
        while(n!=1):
            for i in range(2,int(n+1)):
                a=n/i
                p=a-int(a)
                if p!=0 :
                    continue
                else:
                    x.append(i)
                    n=a
                    break
        if (len(x)==2):
            l1.append(j)
    return(l1)
#15
def prime(n):    
    for i in range(2,int(n/2)+1): 
        if(n%i==0):
            return 0
    return 1
def getSophieGermainPrime(startLimit,endLimit):
    l1=[]
    p,r=startLimit,endLimit
    if p==1:
        p=2
    for a in range(p,r+1):
        k=0     
        for i in range(2,int(a/2)+1): 
            if(a%i==0):
                k=k+1     
                break
        if(k<=0):  
            x=prime(2*a+1)
            if(x==1):
                l1.append(a)
    return(l1)
#16
def getTwinPrime(startLimit,endLimit):
    p,r=startLimit,endLimit
    l1=[]
    q=[]
    if p==1:
        p=2
    x=''
    y=''
    for a in range(p,r+1):
        k=0     
        for i in range(2,int(a/2)+1):
            q=[]
            if(a%i==0):
                k=k+1     
                break
        if(k<=0):  
            if(x==''):
                x=int(a)
                continue
            if(y==''):
                y=int(a)
                if((y-x)==2):
                    q.append(x)
                    q.append(y)
                l1.append(q)
            else:
                x=y
                y=a
                if((y-x)==2):
                    q.append(x)
                    q.append(y)
                l1.append(q)
    l1 = [x for x in l1 if x != []]
    return l1
#17
def getWagstaffPrime(startLimit,endLimit):
    l1=[]
    p,r=startLimit,endLimit
    import math
    if p==1:
        p=2
    for a in range(p,r+1):
        k=0     
        for i in range(2,int(a/2)+1): 
            if(a%i==0):
                k=k+1     
                break
        if(k<=0): 
            x=a        
            a*=3
            a-=1
            a=math.log2(a)
            if(a-int(a)==0):
                l1.append(x)
    return(l1)
#18
def getWieferichPrime(startLimit,endLimit):
    p,r=startLimit,endLimit
    l1=[]
    from fractions import Fraction
    if p==1:
        p=2
    for a in range(p,r+1):
        k=0     
        for i in range(2,int(a/2)+1): 
            if(a%i==0):
                k=k+1     
                break
        if(k<=0):  
            x=a*a
            y=2**(a-1)-1
            z=Fraction(y,x)
            z=(z)-int(z)
            if(z==0.0):
                l1.append(a)
    return(l1)
#19
def getWilsonPrime(startLimit,endLimit):
    p,r=startLimit,endLimit
    l1=[]
    from fractions import Fraction
    import math
    if p==1:
        p=2
    for a in range(p,r+1):
        k=0     
        for i in range(2,int(a/2)+1): 
            if(a%i==0):
                k=k+1     
                break
        if(k<=0):  
            x=a*a
            y=math.factorial(a-1)+1
            z=Fraction(y,x)
            z=(z)-int(z)
            if(z==0.0):
                l1.append(a)
    return(l1)
#20
def check_Prime(a):
    k=0
    if a==1:
        return 0
    for i in range(2,int(a/2)+1): 
        if(a%i==0):
            k=k+1     
            break
    if(k<=0):         
        return 1
    else:
        return 0
#21
def check_Not_Prime(a):
    k=0
    if a==1:
        return 1
    for i in range(2,int(a/2)+1): 
        if(a%i==0):
            k=k+1     
            break
    if(k<=0):         
        return 0
    else:
        return 1
#22
def getLeftTruncatablePrime(startLimit,endLimit):
    t,r=startLimit,endLimit
    q=[]
    for a in range(t,r+1):
        f=0
        w=0
        z=a
        if(check_Prime(a)):
            w=1
            a=str(a)
            p=list(a)
            for i in range(1,len(p)):
                a=len(p)-i-1
                sum=0
                for j in range(i,len(p)):
                    sum=sum+int(p[j])*pow(10,a)
                    a=a-1
                    if(check_Not_Prime(sum)):
                        f=1
        if(f==0 and w==1):
            q.append(z)
    return(q)
#23
def getRightTruncatablePrime(startLimit,endLimit):
    p,r=startLimit,endLimit
    q=[]
    for a in range(p,r+1):
        x=a
        f=0
        while(a>0):
            if(check_Not_Prime(a)):
                f=1
                break
            a=int(a/10)
        if f==0:
            q.append(x)
    return(q)
#24
def getTruncatablePrime(startLimit,endLimit):
    p,r=startLimit,endLimit
    l11=getLeftTruncatablePrime(p,r)
    l12=getRightTruncatablePrime(p,r)
    l1=list(set(l11) | set(l12))
    l1.sort()
    return(l1)
#25
#p=int(input("enter A :"))
#q=int(input("enter B :"))
#print("gausian number is of form A+iB")
def checkGaussianPrime(realPart,imaginaryPart):
    p,q = realPart,imaginaryPart
    if (p==0 and abs(q)%4==3) or (abs(p)%4==3 and q==0):
      f=1
    else:
      x = p**2+q**2
      f=1
      for i in range(2,(x//2)+1):
          if x%i==0:
              f=0
    if f==1:
        print(p," + i * ",q,": is Gaussian Prime",sep="")
    else:
        print("Number is not Gaussian Prime")
#26
def getRandomPrime(primeType,totalDigits,mode=0):
    from primelibpy import RandomFun as r
    x=r.gen_Random(primeType,totalDigits,mode)
    if type(x)==list:
        return(x)
    else:
        return(int(x))
#Factorizations
#27
def getFactorTraditional(semiPrime):
    l1=[]
    from decimal import Decimal
    for i in range(2,int(semiPrime+1)):
        a=Decimal(semiPrime)/i
        p=a-int(a)
        if p!=0 :
            continue
        else:
            l1.append(i)
            l1.append(int(a))
            break
    return l1
    
#28
def getFactorFermatTheorem(semiPrime):
    import gmpy2
    for x in range(int(gmpy2.sqrt(semiPrime))+1,semiPrime,1):
        y=x*x-semiPrime
        if(gmpy2.is_square(y)):
            p=gmpy2.sqrt(y)
            s=x+p
            t=x-p
            return(int(s),int(t))
#29
def gcd(x, y): 
   while(y): 
       x, y = y, x % y 
   return x 
def getFactorPollardRho(semiPrime):
    import random
    x=random.randint(0,100)
    y=x
    c=random.randint(0,100)
    x=(x*x+c)%semiPrime
    p=y*y+c
    y=(p*p+c)%semiPrime
    x1=gcd(abs(x-y),semiPrime)
    while(x1==1):
        x=(x*x+c)%semiPrime
        p=y*y+c
        y=(p*p+c)%semiPrime
        x1=gcd(abs(x-y),semiPrime)
    
    if(x1==semiPrime):
        getFactorPollardRho(int(x1))
    return(x1)
#All 
def getAllFactors(compositeNumber):
    n=compositeNumber
    l1=[1]
    from decimal import Decimal
    for i in range(2,int(n+1)):
        a=Decimal(n)/i
        p=a-int(a)
        if p!=0 :
            continue
        else:
            l1.append(i)
    return l1