class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.top=None
        self.length=0
    def isEmpty(self):
        return (self.top==None)
    def push(self,data):
        temp=Node(data)
        temp.next=self.top
        self.top=temp
        self.length+=1
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty."
        temp=self.top
        self.top=self.top.next
        temp.next=None
        self.length-=1
        return temp.data
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty."
        return self.top.data
    def size(self):
        return self.length