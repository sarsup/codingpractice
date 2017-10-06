
# coding: utf-8

# In[ ]:

class BinaryHeap(object):
    
    def __init__(self,reverse=False):
        self.heaplist = [0]
        self.heapSize = 0
        self.reverse = reverse
        
    def insert(self,val):
        self.heaplist.append(val)
        self.heapSize+=1
        self.percUp(self.heaplist.index(val))
        
    def percUp(self,i):
        while i//2>0:
            if self.reverse: #MaxHeap (parent > child)
                if self.heaplist[i//2] < self.heaplist[i]:
                    self.heaplist[i],self.heaplist[i//2] = self.heaplist[i//2],self.heaplist[i]
            else: #MinHeap (parent<child)
                if self.heaplist[i//2] > self.heaplist[i]:
                    self.heaplist[i],self.heaplist[i//2] = self.heaplist[i//2],self.heaplist[i]
            i = i//2
            
    def minChild(self,i):
        if i*2 + 1 >self.heapSize:
            return i*2
        else:
            if self.heaplist[i*2] > self.heaplist[i*2+1]:
                return i*2 + 1
            else:
                return i*2
    
    def maxChild(self,i):
        if i*2 + 1 > self.heapSize:
            return i*2
        else:
            if self.heaplist[i*2] > self.heaplist[i*2 +1]:
                return i*2
            else:
                return i*2 + 1
            
    def percDown(self,i):
        if self.reverse:
            while i*2 <=self.heapSize:
                mc = self.maxChild(i)
                if self.heaplist[i] < self.heaplist[mc]:
                    self.heaplist[i],self.heaplist[mc] = self.heaplist[mc], self.heaplist[i]
                i = mc
        else:
            while i*2 <=self.heapSize:
                mc = self.minChild(i)
                if self.heaplist[i] > self.heaplist[mc]:
                    self.heaplist[i],self.heaplist[mc] = self.heaplist[mc], self.heaplist[i]
                i = mc
                
            
    def delMin(self):
        retval = self.heaplist[1]
        self.heaplist[1] = self.heaplist.pop()
        self.heapSize-=1
        self.percDown(1)
        return retval
    
    def buildHeap(self, alist):
        self.heaplist = [0] + alist[:]
        self.heapSize = len(alist)
        i = len(alist)//2
        while(i>0):
            self.percDown(i)
            i-=1
    def getRoot(self):
        if self.heapSize>0:
            return self.heaplist[1]
        else:
            return 0
        
    


# In[ ]:

a = [1,2,3,4,5,6,7,8,9,10]
minHeap = BinaryHeap()
maxHeap = BinaryHeap(reverse=True)

for i,e in enumerate(a):
    if i==0:
        temp = e
        print "%.1f" %e
    elif i==1:
        if e>temp:
            maxHeap.insert(temp)
            minHeap.insert(e)
        else:
            maxHeap.insert(e)
            minHeap.insert(temp)
        print "%.1f" %((temp+e)/2.0)
    else:
        rMax = maxHeap.getRoot()
        if e>rMax:
            minHeap.insert(e)
        else:
            maxHeap.insert(e)
        nMin = minHeap.heapSize
        nMax = maxHeap.heapSize
        diff = nMax - nMin
        if abs(diff) > 1:
            if diff<0:
                maxHeap.insert(minHeap.delMin())
            else:
                minHeap.insert(maxHeap.delMin())                
        nMin = minHeap.heapSize
        nMax = maxHeap.heapSize
        rMax = maxHeap.getRoot()
        rMin = minHeap.getRoot()

        if nMin == nMax:
            currmedian = (rMax+rMin)/2.0
        elif nMin>nMax:
            currmedian = rMin
        else:
            currmedian = rMax
        print "%.1f" %currmedian
                        

