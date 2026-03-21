#1
d={"name":"Akshita Gupta","age":20,"gender":"Female"}
print(d)
print(type(d))
#2
for key in d:
    print(d[key])
#3
l=list(d)
print(l)
#4
d["age"]=21
print(d)
#5
print(d.keys())
#6
d2={
    "stu1":{
        "name":"Akshita Gupta",
        "age":20,
        "gender":"Female"
        },
    "stu2":{
        "name":"Akshat Gupta",
        "age":23,
        "gender":"Male"
        },
     "stu3":{
        "name":"Akash Gupta",
        "age":26,
        "gender":"Male"
        }
}
print(d2)
#7
stu1={
        "name":"Akshita Gupta",
        "age":20,
        "gender":"Female"
        }
stu2={
        "name":"Akshat Gupta",
        "age":23,
        "gender":"Male"
        }
stu3={
        "name":"Akash Gupta",
        "age":26,
        "gender":"Male"
        }
new_stu={1:stu1,2:stu2,3:stu3}
print(new_stu)
#8
l1=[1,2,3]
l2=['A','B','C']
new_d={}
i=0
for key in l1:
    new_d[key]=l2[i]
    i+=1
print(new_d)
#9
dx = {"a": 1, "b": 2}
dy = {"c": 3, "d": 4}
dx.update(dy)
print(dx)
#10
sample_dict = {
'C': 92,
'Java': 66,
'Python': 85
} 
min_key = None
min_value = None
for key in sample_dict:
    if min_value is None or sample_dict[key] < min_value:
        min_value = sample_dict[key]
        min_key = key
print("Key with lowest value:", min_key)