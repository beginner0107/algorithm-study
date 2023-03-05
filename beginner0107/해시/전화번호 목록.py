def solution(phone_book):
    s = dict()
    for p in phone_book:
        for i in range(1, len(p)):
            s[p[:i]] = 1

    for p in phone_book:
        if p in s:
            return False
    return True