'''
def solution(orders, course):
    cnt = dict()
    result=[]
    
    from itertools import combinations as c
    
    for cour in course:
        #order의 최대 길이 < course의 길이인 경우 코스 없음
        if len(sorted(orders, key=len)[-1])<cour:
            continue
            
        combi=[]
        for text in orders:            
            combi.extend(list(c(sorted(text),r=cour)))
        
        for com in set(combi):
            temp=''.join(sorted(com))
            for order in orders:               
                if not set(com)-set(order):
                    if temp in cnt:
                        cnt[temp]+=1
                    else:
                        cnt[temp]=1
        
        #최소 2가지 이상의 단품메뉴 구성
        maxcnt=max(cnt.values())
        if maxcnt<2:
            continue
        
        sort_cnt=sorted(list(cnt.items()), \
                        key=lambda x:x[1], reverse=True)
        
        for i,j in sort_cnt:
            if j!=maxcnt:
                break
            else:
                result.append(i)
                
        cnt=dict()
        
    return sorted(result)
'''

from collections import Counter
from itertools import combinations 

def solution(orders, course):
    result=[]
    
    for cour in course:
        if len(sorted(orders, key=len)[-1])<cour:
            continue
        
        combi=[]
        for order in orders:
            combi.extend(list(combinations(sorted(order),r=cour)))
        
        order_lst=Counter(combi).most_common() #sort
        max_order=order_lst[0][1]
        
        if max_order<2:
            continue
            
        for i in range(len(order_lst)):
            if order_lst[i][1]!=max_order:
                break
            else:
                result.append(''.join(order_lst[i][0]))
    return sorted(result)
                
                         
