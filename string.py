#1
y=input("Enter a String: ")
z="hi"
print(y)
print(z)
#2
s="TasinCoder"
print(s[:5])
#3
s1="HelloLearners"
print(s[2:6])
#4
a="Learning" 
b="Python"
print(a+" "+b)
#5
c=0
for i in range(len(s)):
    c=c+1
print(c)
#6
print(s[: :-1])
#7
s3="Coder"
if s3 in s:
    print("Substring is present")
#8
new_s="1234as"
print(new_s.isdigit())
#9
print(new_s.isalpha())
#10
a=2234566
print(type(str(a)))
