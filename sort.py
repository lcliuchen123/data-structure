
def sort(nums):
    k=len(nums)
    for  i in range(k):
        for j in range(k-i-1):
            if nums[j+1]<nums[j]:
                tmp=nums[j+1]
                nums[j+1]=nums[j]
                nums[j]=tmp
    return nums

#选择排序:每次都选择一个最小的元素
def sort2(nums):
    k=len(nums)
    for i in range(k):
        minIndex=i
        for j in range(i+1,k):
            if nums[j]<nums[minIndex]:
                minIndex=j

        if minIndex!=i:
            nums[i],nums[minIndex]=nums[minIndex],nums[i]
    return nums

def sort3(nums,begin,end):
    if begin>=end:
        return
    i=begin
    j=end
    tmp=nums[i]
    while i<j:
        while i<j and  nums[j]>=tmp:
            j=j-1
        if i<j:
            nums[i]=nums[j]
            i=i+1
        while i<j and  nums[i]<=tmp:
            i=i+1
        if i<j:
            nums[j]=nums[i]
            j=j-1
    nums[i]=tmp
    sort3(nums,begin,i-1)
    sort3(nums,i+1,end)

    return nums


nums=[1,2,5,3,4]
print(sort3(nums,0,4))