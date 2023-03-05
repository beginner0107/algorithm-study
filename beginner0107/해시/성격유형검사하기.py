def solution(survey, choices):
    answer = ''
    s = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    c = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}

    for i in range(len(survey)):
        a = survey[i][0]
        b = survey[i][1]

        if choices[i] <= 3:
            s[a] += c[choices[i]]
        elif 4 < choices[i] <= 7:
            s[b] += c[choices[i]]
    li = list(s.keys())
    for i in range(0, len(li), 2):
        num1 = s[li[i]]
        num2 = s[li[i + 1]]
        if num1 > num2:
            answer += li[i]
        elif num1 < num2:
            answer += li[i + 1]
        else:
            if ord(li[i]) < ord(li[i + 1]):
                answer += li[i]
            else:
                answer += li[i + 1]

    return answer

