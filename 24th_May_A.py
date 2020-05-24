for _ in range(int(input())):
    x, y =map(int,input().split())
    if(x==y):
        ans = 2*x
        fin_ans = ans**2
        print(fin_ans)
    elif(2*x>y and 2*y<=x):
        ans = x**2
        print(ans)
    elif(2*y>x and 2*x<=y):
        ans = y**2
        print(ans)
    elif(2*x>y and 2*y>x):
        p = min(x,y)
        ans = 2*p
        fin2 = ans**2 
        print(fin2)
