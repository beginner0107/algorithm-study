def solution(elements): # 시각 복잡도 O(n ^ 2) -> n의 최대값 1000 -> 10^6
    answer = set()
    el = len(elements)
    elements = elements * 2
    for i in range(el):
        for j in range(el):
            answer.add(sum(elements[j:j + i + 1]))
    return len(answer)