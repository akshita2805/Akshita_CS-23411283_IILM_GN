def binary_search(arr,num):
    low=0
    high=len(arr)-1
    while low<=high:
        mid =low+high//2
        if arr[mid]==num:
            return mid
        elif arr[mid]<num:
            low=mid+1
        else:
            high=mid-1
    return -1

arr=[2,3,4]
num=3
result=binary_search(arr,num)
print(result)

        
