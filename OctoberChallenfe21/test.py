def generateSubArrays(arr,subarr,start,end):
    if end==len(arr):
        return subarr
    elif start>end:
        return generateSubArrays(arr,subarr, 0, end+1)
    else:
        subarr.append(arr[start:end+1])
        return generateSubArrays(arr,subarr, start+1, end)


def mexarr(arr):
    arr=sorted(arr)
    for i in range(len(arr)):
        if arr[i]!=i:
            return i
    return len(arr)


print(mexarr([0,1,2,3,4,5,6,7,8,9]))