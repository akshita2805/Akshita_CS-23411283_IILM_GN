nums = [2,2,1,1,1,2,2]
def func(nums):
    d={}
    c=0
    for i in range(len(nums)):
        if nums[i] in d:
            d[nums[i]]+= 1
        else:
            d[nums[i]]= 1
    k=None
    for key in d:
        if d[key]>c:
            c=d[key]
            k=key
    return k
print(func(nums))
        
