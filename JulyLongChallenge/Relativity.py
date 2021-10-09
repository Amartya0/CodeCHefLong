for i in range(int(input())):
    #take 2 integer variables from input
    g, c = map(int, input().split())
    #calculate c^2/2*g
    print(int(c**2/(2*g)))