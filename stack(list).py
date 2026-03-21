class stack:
    def __init__(self):
        self.top=[]
    def push(self,data):
        self.top.append(data)
    def pop(self):
        if len(self.top):
            return self.top.pop()
        return "Stack is Empty."
    def peek(self):
        if len(self.top):
            return self.top[-1]
        return "Stack is Empty."
    def size(self):
        if len(self.top):
            return len(self.top)
        return "Size is 0."
    def isEmpty(self):
        return not(len(self.top))
s=stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(s.peek())

        
        