def solution(record):
    answer = []
    info={}
    
    for rec in record:
        try:
            inout,user,nick=rec.split()
            info[user]=nick
        except:
            inout,user=rec.split()
            
        answer.append(rec.split())
        
    result=[]
    for rec in answer:
        if rec[0]=="Change":
            continue
        elif rec[0]=="Enter":
            result.append(info[rec[1]]+"님이 들어왔습니다.")
        else:
            result.append(info[rec[1]]+"님이 나갔습니다.")
            
    return result
