def check(a,b,c,d,e):
    if (a+b <= d and c <= e) or (b+c <= d and a <= e) or (c+a <= d and b <= e):
        return 'YES'
    return 'NO'

    
for _ in range(int(input())):
    a,b,c,d,e = list(map(int, input().split()))
    
    print(check(a,b,c,d,e))