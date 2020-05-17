
for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    if(b>=a):
        print(b)
    elif(d>=c):
        if(b>a):
            print(b)
        else:
            print('-1')
    elif(b+c>=a+d):
        print(b+c)
    
    else:
        sleep = b
        time = b
        if((a-b)%(c-d)==0):
            n = (a-b)//(c-d)
            time = b+n*c
            print(time)
        else:
            n = (a-b)//(c-d) + 1 
            time = b+n*c
            print(time)