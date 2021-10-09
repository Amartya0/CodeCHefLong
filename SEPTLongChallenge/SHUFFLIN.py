for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    a_evens = 0
    a_odds = 0
    for i in l:
        if i%2 ==0 :
            a_evens += 1
        else:
            a_odds += 1
    b_evens, b_odds = [n/2, n/2] if n%2==0 else [(n-1)/2, (n+1)/2]
    result = 0
    if a_evens > b_odds:
        result += b_odds
    else:
        result += a_evens
        
    if a_odds > b_evens:
        result += b_evens
    else:
        result += a_odds
    
    
    print(int(result))