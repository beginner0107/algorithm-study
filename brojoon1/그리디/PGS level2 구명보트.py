'''

EX)
people 리스트 정렬
=> 40 50 60 70 80 90 100

Limit - 제일 가벼운 사람 >= 제일 가벼운 사람과 같이 구명 보트 탈 가장 무거운 사람

즉, 40 선택후 100, 90, 80, 70, 60, 50 순으로 돌면서 같이 탈 수 있는 사람이 있으면 선택

'''

def solution(people, limit):
    people.sort()
    
    cnt = 0
    start = 0
    end = len(people) -1

    while start <= end:
        # 같이 타고 가는 경우
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
            cnt += 1
        # 혼자 타고 가는 경우
        else:
            end -= 1
            cnt += 1
        
    return cnt