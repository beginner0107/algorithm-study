# (Greedy) 프로그래머스 Lv1 42862 체육복 문제
# n: 전체 학생수, lost: 체육복 도난당한 학생 list, reserve: 여벌 체육복 보유한 학생 list

def solution(n, lost, reserve):
    
    ans = n    # 모든 학생이 수업 가능한 것으로 초기화
    borrow = []    # 여벌 체육복 있으나, 도난 당해 빌려줄 수 없는 학생리스트
    
    # lost, reserve 리스트 정렬
    lost.sort()
    reserve.sort()
    
    # 여벌 있는데 도난당한 학생 먼저 제외
    for l in lost:
        if l in reserve:
            borrow.append(l)
    for b in borrow:
        lost.remove(b)
        reserve.remove(b)
    
    # 앞, 뒤 학생에게 체육복 빌릴 수 있는지 확인
    # 없다면, ans - 1
    for l in lost:
        if (l - 1) in reserve:
            reserve.remove(l - 1)
        elif (l + 1) in reserve:
            reserve.remove(l + 1)
        else:
            ans -= 1
    
    return ans