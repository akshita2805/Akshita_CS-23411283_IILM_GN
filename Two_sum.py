arr=[18,19,8,7,6,7]
n=len(arr)
target=15
def func(arr,X):
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==X:
                return i,j

print(func(arr,target))
