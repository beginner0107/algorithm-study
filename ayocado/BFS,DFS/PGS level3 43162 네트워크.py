def solution(n, computers):
    stack = []
    dict_com = {}
    visited = [[0] * n for _ in range(n)]
    answer = 0

    for i in range(n):
        dict_com[i] = [idx for idx, num in enumerate(computers[i]) if num == 1]

    for keys in list(dict_com.keys()):
        count = 0
        if len(dict_com[keys]) == 1:
            answer += 1
            print('one')
        else:
            for values in dict_com[keys]:
                if values != keys and visited[keys][values] != 1:
                    stack.append([keys, values])
                    visited[keys][values] = 1
                    visited[values][keys] = 1
                    count += 1

            while stack:
                row, col = stack.pop()

                for col_ in dict_com[col]:
                    if visited[col][col_] != 1 and col != col_:
                        stack.append([col, col_])
                        visited[col][col_] = 1
            if count > 0:
                answer += 1

    return answer
