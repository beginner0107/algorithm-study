def solution(dirs):
    # 좌표계
    answer = 0
    path_set = set()
    y, x = 0, 0
    for dir in dirs:
        if dir == "U" and y < 5:
            path_set.add((y, x, y+1, x))
            y += 1
        elif dir == "D" and y > -5:
            path_set.add((y-1, x, y, x))
            y -= 1
        elif dir == "R" and x < 5:
            path_set.add((y, x, y, x+1))
            x += 1
        elif dir == "L" and x > -5:
            path_set.add((y, x-1, y, x))
            x -= 1
    answer = len(path_set)
    return answer
