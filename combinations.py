# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 22:41:56 2018

@author: tao
""" 
from itertools import combinations
ary=[745,298,318,380.2,624.6,216.2,499,399,1923,99.5,245,578.7,973,506.8,94,164.7,433,441.5,419,165,1196,245,999]
sum=0
k=0
j=7
diff=1
fo=open('C:\work\MyResultforJDPailieZuhe.txt','w')
fo.write('\n\n\n                                                   符合要求的结果如下所示：\n')
while j<=17:
    #如果找到一个结果就退出，则下面的注释改为代码即可
    #if k>=1:
     #   break
    i=0
    lst=list(combinations(ary, j))
    print('由'+str(j)+'个元素组成的结果有以下\n')
    fo.write('由'+str(j)+'元素组成的结果如下：\n')
    for a in lst:
        for b in a:
            sum=sum+b
        diff=abs(sum-6194.0)
        if (diff<=0.01):
            #print(sum)
            print(lst[i])
            #每找到一个符合要求的组合，k+1,k为找到的个数
            k+=1
            #sumstr=str(sum)
            lstr=str(lst[i])
            fo.write(lstr+'\n')
            #如果找到符合要求的内容就停止，去掉下面的注释
            #break
        i+=1
        sum=0
    j+=1
print('一共找到了',k,'个符合要求的组合')
k=str(k)
fo.seek(0,0)
fo.write('一共找到了'+k+'个符合要求的结果，内容如下\n')
fo.close()
