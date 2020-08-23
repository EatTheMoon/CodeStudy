"""
《《小美的跑腿代购
看着不像是动态规划...
把价格＋２*重量和订单号存入列表后，对列表进行订单号从小到大，价值从大到小排序
输出前m项的订单号就完事了=.=
结果好像只是18%
"""
n,m = map(int,input().split())
val_wei_list = []
for i in range(n):
    val,weight = map(int,input().split())
    val_wei_list.append((val+weight*2,i+1))
val_wei_list = sorted(val_wei_list,key=lambda x:x[1])
val_wei_list = sorted(val_wei_list,key=lambda x:x[0],reverse=True)
#print(val_wei_list)
for i in range(m):
    print(val_wei_list[i][1],end=" ")
    

