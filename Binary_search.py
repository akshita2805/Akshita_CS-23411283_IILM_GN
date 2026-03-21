def binary_search(arr,n):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=low+high//2
        if(arr[mid]==n):
            return mid
        elif(arr[mid]<n):
            low=mid+1
        else:
            high=mid-1
    return -1
        
array=[10,20,30,40,50,60]
num=40
result=binary_search(array,num)
print(result)



