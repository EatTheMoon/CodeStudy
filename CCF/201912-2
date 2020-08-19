n = int(input())
location = []
result = [0]*5
for i in range(n):
    x,y = list(map(int,input().split()))
    location.append((x,y))

for loc in location:
    if (loc[0]-1,loc[1]) in location and (loc[0]+1,loc[1]) in location and (loc[0],loc[1]-1) in location and (loc[0],loc[1]+1) in location:
        ans = 0
        if (loc[0]-1,loc[1]+1) in location:
            ans += 1
        if (loc[0]-1,loc[1]-1) in location:
            ans += 1
        if (loc[0]+1,loc[1]-1) in location:
            ans += 1
        if (loc[0]+1,loc[1]+1) in location:
            ans += 1
        result[ans] += 1

for i in result:
    print(i)

