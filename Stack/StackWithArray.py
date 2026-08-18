class Stack:
    def __init__(self,size):
        self.size = size
        self.arr = [-1] * size
        self.top = -1
    
    def push(self,data):
        if(self.top < self.size-1):
            self.top += 1
            self.arr[self.top] = data
        else:
            print("STACK IS FULL")
    
    def pop(self):
        if(self.top > -1):
            val = self.arr[self.top]
            self.arr[self.top] = -1
            self.top -= 1
            return val
        else:
            print("STACK IS EMPTY")
    
    def empty(self):
        if(self.top == -1):
            print("STACK IS EMPTY")
        else:
            print("STACK IS NOT EMPTY")
    
    def printStack(self):
        if(self.top == -1):
            print("STACK IS EMPTY")
        i = 0
        while(i<=self.top):
            print(self.arr[i])
            i+=1


s = Stack(5)
# s.empty()
# s.printStack()
# s.pop()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.empty()
s.printStack()
print("---------------POPPING PRINTS----------------")
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
# s.pop()
s.empty()
s.printStack()