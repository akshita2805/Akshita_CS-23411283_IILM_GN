s2={"Akshita Gupta","20","Female"}
print(s2)
print(type(s2))
thisset={"Java","Python","Django"}
if "Python" in thisset:
    print("Present")
secondset={"C","Cpp","NoSQL"}
temp_set=thisset.union(secondset)
print(temp_set)
mylist=["Java","C"]
temp_set2=thisset.union(set(mylist))
print(temp_set2)
new_set={"Python","Django","JavaScript","SQL"}
print(new_set.pop())
print(new_set)
new_set.clear()
print(new_set)
n_set={"Python","Django","JavaScript","SQL"}
for i in n_set:
    print(i)
s3={33,345,67,89,1000}
print(min(s3))
print(max(s3))