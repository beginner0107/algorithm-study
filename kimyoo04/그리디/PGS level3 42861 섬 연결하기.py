# https://school.programmers.co.kr/learn/courses/30/lessons/42861?language=python3

"""
핵심
- 크루스칼 알고리즘을 사용하기
- cost를 기준으로 정렬
- Union-Find 자료구조 (set 자료구조) 사용
- 모든 n개의 섬이 연결되려면 간선의 수는 n-1개
"""

def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2])

    # Union-Find 자료구조로 가장 cost가 작은 시작점 넣기
    link = set([costs[0][0]])

    # 모두 연결 되고나서 n-1개를 초과 못함
    while len(link) != n:
        # 그리디 탐색
        for v in costs:
            # 서로소 집합에 모두 있으면 continue (사이클 형성)
            if v[0] in link and v[1] in link:
                continue
            # 서로소 집합에 하나 이하가 있다면
            if v[0] in link or v[1] in link:
                # update로 여러개 값 한번에 추가
                link.update([v[0], v[1]])
                answer += v[2]
                break

    return answer