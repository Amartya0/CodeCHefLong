for i in range(int(input())):
    #take 4 variable from input as integer
    d, x, y, z = map(int, input().split())
    #take two integer varibale as result  7*x and (d*y+(7-d)*z)
    result2 = (d*y+(7-d)*z)
    result1 = 7*x
    # If result1 is greater than result2 print result1, else print result2
    if result1 > result2: print(result1)
    else: print(result2)

        

