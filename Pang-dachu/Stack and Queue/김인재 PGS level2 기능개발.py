from collections import deque 

def solution(progresses, speeds):
    result = [] 
    
    progress = deque(progresses)
    speeds   = deque(speeds)
    
    while progress :
        cnt = 0
        
        for i in range(len(speeds)) :
            progress[i] += speeds[i] 

        while True :
            try :
                if progress[0] >= 100 :
                    progress.popleft()
                    speeds.popleft()
                    cnt += 1
                else :
                    break
            except IndexError :
                break
        
        if cnt > 0 : 
            result.append(cnt)

            
    return result
        
            
        