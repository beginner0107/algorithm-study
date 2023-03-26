def checked(arr, x, y, size):
    value = arr[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if value != arr[i][j]:
                return False
    return True


def divided(arr, answer, x, y, size):
    if checked(arr, x, y, size):
        answer[arr[x][y]] += 1
        return
    newSize = size // 2
    divided(arr, answer, x, y, newSize)
    divided(arr, answer, x + newSize, y, newSize)
    divided(arr, answer, x, y + newSize, newSize)
    divided(arr, answer, x + newSize, y + newSize, newSize)


def solution(arr):
    answer = list([0, 0])
    divided(arr, answer, 0, 0, len(arr))
    return answer
