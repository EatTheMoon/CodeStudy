n,m = map(int,input().split())
l = []

for i in range(n):
    info_li = list(map(int,input().split()))
    l.append((i+1,info_li))

sum_ = 0
max_,index = 0,0
for i in l:
    sum_ += sum(i[1])
    if abs(sum(i[1][1:m+1]))>max_:
        index = i[0] 
        max_ = abs(sum(i[1][1:m+1]))

print(sum_,index,max_)
