for _ in range(int(input())):
    s = input()
    count = 0
    res = [s[i: j] for i in range(len(s)) 
          for j in range(i + 3, len(s) + 1)] 
    lens = list()
    for i in range(len(res)):
        if(res[i].count('1')>=1 and res[i].count('2')>=1 and res[i].count('3')>=1):
            lens.append(len(res[i]))
            count = 1
    lens.sort()
    if (count!=0):
        print(lens[0])
    else:
        print(0)
    