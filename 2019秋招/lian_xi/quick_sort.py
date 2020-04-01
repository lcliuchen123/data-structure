
def sort(nums,begin,end):
    if begin>=end:
        return
    i=begin
    j=end
    tmp=nums[i]
    while i<j:
        while i<j and  nums[j]>tmp:
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

    return nums


if __name__ == "__main__":
    l = [0,1,1,1,1,0,1,0]
    print(sort(l,0,len(l)-1))
