
# coding: utf-8

# In[38]:

import copy
tres=[]
with open("output02.txt","r") as opfile:
    for line in opfile:
        tres.append(line.replace('\n',''))
with open("input02.txt","r") as testfile:
    nCases = int(testfile.readline())
    j=0
    res = []
    for line in testfile:
        j+=1
        if j%3==1:
            m = int(line)
        elif j%3 == 2:
            n = int(line)
        elif j%3 == 0:
            a = [int(s) for s in line.split()]
            cdict = {}
            for i,e in enumerate(a):
                if not cdict.get(e):
                    cdict[e] = [i+1]
                else:
                    cdict[e].append(i+1)
            for i,e in enumerate(a):
                if cdict.get(m-e):
                    
                    x = [d for d in cdict[m-e] if d != i+1]
                    if len(x)>0:
                        res.append(str(i+1)+" "+str(x[0]))
                    else:
                        continue
                    if res[len(res)-1]!=tres[len(res)-1]:
                        print "gotcha"
                        pp=copy.copy(a)
                        xdict = copy.copy(cdict)
                        tot = m
                        print res[len(res)-1], tres[len(res)-1]
                        raise ValueError
                    break
                
for i in range(50):
    if res[i]!=tres[i]:
        print "ind=%d, res=%s, tres=%s" %(i,res[i],tres[i])            
        
        

