#1
def func1():
    print("TasiNCoder")
func1()
#2
def func2(a,b):
    print(a+b)
func2(1,2)
#3
def func3(*varargs):
    s=0
    for i in varargs:
        s=s+i
    print(s)
func3(1,2,3)
#4
def func4(**kwargs):
    for key in kwargs:
        print(key)
func4(name="Akshita", age=20, course="Data Science")
#5
def func5(l):
    print(l)
print([1,2,3,4])
#6
def func6(a,b,c,d):
    max_num=a
    if b>max_num:
        max_num=b
    if c>max_num:
        max_num=c
    if d>max_num:
        max_num=d
    return max_num
print(func6(1,2,4,3))
#7
def func7(l):
    s=0
    for i in l:
        s+=i
    return s
print(func7([1,2,3]))
#8
def func8(l):
    m=1
    for i in l:
        m*=i
    return m
print(func7([1,2,3]))
#9
def func8(n,start,end):
    for i in range(start,end+1):
        if n ==i:
            return True 
        return False
print(func8(15,1,10))
#10
def func10(n):
    if n%2==0:
        return True
    return False
print(func10(2))


#1
def f1(l):
    s=set(l)
    new_l=list(s)
    return new_l
l=[1,1,2,4,5,6,6]
print(f1(l))
#2
def f2(n):
    if n==0 or n==1:
        print("Not Prime")
        return
    for i in range(2,n):
        if n%i==0:
            print("Not Prime")
            return
    print("Prime")
f2(4)
#3
def f3(l):
    new_l=[]
    for i in l:
        if i%2==0:
            new_l.append(i)
    return new_l
print(f3([1,2,3,4,5,6,7,8,9]))
#4
def f4(s):
    s=s.lower()
    if s==s[ : :-1]:
        return True
    else:
        return False
print(f4("Madam"))
print(f4("Hello"))
#5
def f5(n1,n2,n3):
    mini=n1
    if n2<mini:
        mini=n2
    if n3<mini:
        mini=n3   
    return mini
print(f5(4,1,6))     
#6
def f6():
    l=[]
    for i in range(1,31):
        l.append(i*i)
    return l
print(f6())
#7
def f6(a,b):
    def f66():
        return a+b
    s=f66()
    return s
print(f6(4,5))
#8
def f8(s):
        u,l=0,0
        for i in range(len(s)):
            if s[i].isupper():
                u=u+1
            elif s[i].islower():
                l=l+1
        return u,l
u,l=f8("IILM uNIVERSITY")
print(f"No of Upper Case letters: {u}  No of Lower Case letters: {l}")
#9


        





        
