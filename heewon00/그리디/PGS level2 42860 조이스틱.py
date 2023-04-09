def solution(name):
    answer = 0
    
    joy=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    n_lst=[]
    
    for n in name:
        n_th=joy.index(n)
        if n_th>13: n_th=26-n_th
        answer+=n_th ; n_lst.append(n_th)
    
    move=len(name)-1
    print(n_lst)
    if 0 not in n_lst:
        return answer+move
    
    for i in range(len(n_lst)):
        next_n = i+1
        while next_n < len(n_lst) and n_lst[next_n]==0:
            next_n+=1
        move= min(move, i*2+len(n_lst)-next_n, \
                  i+2*(len(n_lst)-next_n))
        
    return answer+move
        
        
