    
def northside(xadd,passing):
    x=[]
    x.append(xadd[0])
    x.append(xadd[1])
    xadd.remove(xadd[1])
    xadd.remove(xadd[0])
    xadd.append(x[0]-1)
    xadd.append(x[1])
    c=[]
    c.append(x[0]-1)
    c.append(x[1])
    if(c in passing):
        northside(xadd,passing)
    else:
        passing.append(c)
    
def southside(xadd,passing):
    x=[]
    x.append(xadd[0])
    x.append(xadd[1])
    xadd.remove(xadd[1])
    xadd.remove(xadd[0])
    xadd.append(x[0]+1)
    xadd.append(x[1])
    c=[]
    c.append(x[0]+1)
    c.append(x[1])
    if(c in passing):
        southside(xadd,passing)
    else:
        passing.append(c)

def westside(xadd,passing):
    x=[]
    x.append(xadd[0])
    x.append(xadd[1])
    xadd.remove(xadd[1])
    xadd.remove(xadd[0])
    xadd.append(x[0])
    xadd.append(x[1]-1)
    c=[]
    c.append(x[0])
    c.append(x[1]-1)
    if(c in passing):
        westside(xadd,passing)
    else:
        passing.append(c)

def eastside(xadd,passing):
    x=[]
    x.append(xadd[0])
    x.append(xadd[1])
    xadd.remove(xadd[1])
    xadd.remove(xadd[0])
    xadd.append(x[0])
    xadd.append(x[1]+1)
    c=[]
    c.append(x[0])
    c.append(x[1]+1)
    if(c in passing):
        eastside(xadd,passing)
    else:
        passing.append(c)

def fun(a,b,y,j):
    initialpoint=[]
    initialpoint.append(a)
    initialpoint.append(b)
    directions=y
    passing=[]
    passing.append(initialpoint)
    xadd=[]
    xadd.append(a)
    xadd.append(b)
    for i in range(len(directions)):
        if(directions[i]=='N'):
            northside(xadd,passing)
        elif(directions[i]=='S'):
            southside(xadd,passing)
        elif(directions[i]=='W'):
            westside(xadd,passing)
        elif(directions[i]=='E'):
            eastside(xadd,passing)
    sd=[]
    sd.append(str(xadd[0]))
    sd.append(str(xadd[1]))
    xd=' '.join(sd)
    SE=['Case #',str(j)]
    AS=''.join(SE)
    qw=[AS,':',' ',xd]
    pq=''.join(qw)
    print(pq)
    
n=int(input())
for j in range(n):
    x=list(input().split())
    a=int(x[-2])
    b=int(x[-1])
    y=input()
    fun(a,b,y,j+1)

