def solution(n):
    answer = []

    # 삼각형 만들기
    triangle = [[0] * i for i in range(1, n + 1)]
    x, y = -1, 0
    num = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            triangle[x][y] = num
            num += 1

    # 삼각형 숫자 반환
    for row in triangle:
        answer += row

    return answer
