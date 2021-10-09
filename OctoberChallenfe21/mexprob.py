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



for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    subarry=(generateSubArrays(arr, [], 0, 0))
    ans=[]
    for i in range(len(subarry)):
        ans.append(mexarr(subarry[i]))
    print((sorted(ans))[k-1])