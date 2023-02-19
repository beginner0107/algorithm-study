def solution(numbers):
    return str(int("".join(sorted([str(x) for x in numbers], key=lambda x:x*3, reverse = True))))