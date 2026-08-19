class stack:
    def __init__(self,size):
        self.size = size
        self.arr = [None] * size
        self.top1 = -1
        self.top2 = size
    
    def pushOne(self,data):
        if(self.top1 == self.size - 1 or self.top1 >= self.top2-1):
            print("FULL")
            return
        
        self.top1 += 1
        self.arr[self.top1] = data
    
    def pushTwo(self,data):
        if(self.top2 == 0 or self.top2 <= self.top1 + 1):
            print("Full")
            return
        self.top2 -= 1
        self.arr[self.top2] = data
    
    def popOne(self):
        if(self.top1 == -1):
            return -1
        
        val = self.arr[self.top1]
        self.arr[self.top1] = None
        self.top1 -= 1
        return val
    
    def popTwo(self):
        if(self.top2 == self.size):
            return -1
        
        val = self.arr[self.top2]
        self.arr[self.top2] = None
        self.top2 += 1
        return val
        
