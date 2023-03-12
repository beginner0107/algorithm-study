"""
numbers의 조합으로 만들 수 있는 모든 경우의 수를 다 저장 후,
target의 개수 count

"""

def solution(numbers, target):
    # 전체 경우의 수를 담을 리스트
    all_arr = [0]
    
    for i in numbers:
        # 계산하여 담을 리스트
        sub_arr = []
        
        for j in all_arr:
            sub_arr.append(j+i)
            sub_arr.append(j-i)
        #print(sub_arr)    
        all_arr = sub_arr
        
    #print(all_arr)
    return sub_arr.count(target)