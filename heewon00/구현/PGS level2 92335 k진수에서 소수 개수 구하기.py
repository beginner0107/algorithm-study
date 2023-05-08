import math

def solution(n, k):
    result=0
    
    def trans(n,k):
        digit=''
        while n:
            digit=str(n%k)+digit
            n//=k
        return digit

    def prime(n):
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                return False
        return True
    
    for i in trans(n,k).split('0'):
        if i=='' or i=='1':
            continue
        if prime(int(i)):
            result+=1
            
    return result
