def DFS( ticket, path, result ) :
    # 티켓 리스트가 비었을 때는 모든 티켓을 사용한 경우이므로 
    # 결과중의 하나가 된다. 
    if not ticket : 
        result.append( path )
        
    for index, element in enumerate( ticket ) :
        
        # 현재 도착한 곳 - 가야할 곳 탐색 
        if path[-1] == element[0] :
            # 이 부분도 경우의 수가 여러개 나오므로 
            # 각 경우에 수 마다 티켓과 경로를 복사하여 사용 
            temp_ticket = ticket.copy()
            temp_path   = path.copy() 
            
            temp_path.append( element[1] )
            del temp_ticket[index] 
            
            DFS( temp_ticket, temp_path, result )
        
        else : 
            continue

def solution(ticket):
    result = []
    start_index = []
    path = []
    
    # 시작은 ICN으로 하기 때문에 
    # 시작 지점이 될 수 있는 경우의 index 저장 
    for index , element in enumerate( ticket ) :
        if element[0] == "ICN" :
            start_index.append( index )
        
    # 시작 지점의 경우의 수 만큼 반복 
    for index in start_index :
        
        # 하나의 경우에서 사용되는 ticket과 
        # 저장되는 path가 다르므로 복사본으로 전달 및 사용 
        temp_ticket = ticket.copy()
        temp_path   = path.copy()
        
        # 시작 경로인 ICN 추가 
        # 첫번째 티켓의 도착지 추가 
        temp_path.append( ticket[index][0] )
        temp_path.append( ticket[index][1] )
        
        # 사용된 티켓 제거 
        del temp_ticket[index]
        
        
        DFS( temp_ticket, temp_path, result )
        
    return sorted( result )[0]