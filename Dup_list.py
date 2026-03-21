x=[22,33,44,55,22,33,44,55]
def func(x):
    if len(x)!=len(set(x)):
        return True
    else:
        return False
print(func(x))