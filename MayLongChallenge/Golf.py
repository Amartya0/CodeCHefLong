for i in range(int(input())):
    N,x,k = [int(j) for j in input().split()]
    if((x%k==0) or (((N+1)-x)%k==0)):
        print('Yes')
    else:
        print('No')