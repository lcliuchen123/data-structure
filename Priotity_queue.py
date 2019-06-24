

class Priority_Que:
    def __init__(self, elist=[]):
        self.elems = list(elist)
        self.buildheap()

    def buildheap(self):
        end = len(self.elems)
        for i in range((end-1)//2, -1,-1):
            self.siftdown(self.elems[i],i,end)

    def is_empty(self):
        return not self.elems

    def peek(self):
        if not self.elems:
            return ValueError
        return self.elems[0]

    def siftup(self,e,last):
        # 把元素下沉（写）
        elems, i ,j = self.elems,last, (last-1)//2
        while i>0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j-1)//2
        elems[i] = e

    def enqueue(self, e):
        self.elems.append(None)
        self.siftup(e,len(self.elems)-1)

    def siftdown(self,e,start,end):
        # 写
        if start >= end:
            return
        elems, i, j = self.elems, start, 2*start+1
        while j<end:
            if j+1<end and elems[j] > elems[j+1]:
                j+=1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i,j = j, 2*j+1
        elems[i] = e

    def queue(self):
        elems = self.elems
        e0 = elems[0]
        e= elems.pop()
        if len(elems)>0:
            self.siftdown(e, 0, len(elems))
        return e0

q= Priority_Que([1,4,2,3])
print(q.peek())
print(q.queue())
q.enqueue(5)
print(q.elems)
print(q.elems)