def int2base(x, base):
    digits = []

    while x:
        digits.append(x % base)
        x = x // base

    return int(sum(digits))

for _ in range(int(input())):
    n, l, r = list(map(int, input().split()))
    
    temp = int2base(n, r)
    ans = r
    
    for b in range(r-1,l-1, -1):
        curr = int2base(n, b)
        if curr == 1:
            ans = b
            break
        if curr < temp:
            temp = curr
            ans = b
            
    print(ans)