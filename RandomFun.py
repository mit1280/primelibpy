import Prime as p
import random
def gen_Random(name,n,mode):
    name="get"+name
    if name=="getBalancedPrime":
        x=[]
        while(len(x)==0):
            start = random.randint(10**(n-1),10**n//2)
            end = random.randint((10**n//2)+1,(10**n)-1)
            x = getattr(p,name)(start,end,mode)
        x=list(filter(None, x))
        return(random.choice(x))
    x=[]
    while(len(x)==0):
        start = random.randint(10**(n-1),10**n//2)
        end = random.randint((10**n//2)+1,(10**n)-1)
        x = getattr(p,name)(start,end)
    x=list(filter(None, x))
    return(random.choice(x))
