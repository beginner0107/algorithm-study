"""
● 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12909

    괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어

    "()()" 또는 "(())()" 는 올바른 괄호입니다.
    
    ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
    
    '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.
    
    
● 생각
    스택이나 큐를 적용해야하는지 모르겠음
    조건 1. 앞에서부터 개수를 셀 떄, '(' 개수는 ')' 개수와 같거나 더 많아야함
    조건 2. 개수 집계가 끝났을 때, '(' 개수 == ')' 개수
    
    count : count[0]은 '(' 개수, count[1]은 ')' 개수
"""
def solution(s):
    
    count = [0,0]
    
    for i in s:
        if i == '(':
            count[0] += 1
        else:
            count[1] += 1
            
        if count[1] > count[0]:
            return False
    
    if count[1] != count[0]:
        return False
    else:
        return True

"""
● 다른 풀이
    try ~ except 이용한 풀이
    1. '(' 면, 리스트에 추가
    2. ')' 면, 리스트에서 pop
    3. ')' 이 더 많으면 안된다 -> pop을 할 때 오류가 발생하면 안됨 -> 오류 발생 시, false
    4. 마지막에는 리스트에 남은 원소가 없어야함( '(' , ')' 개수는 같기 때문)
"""
def is_pair(s):
    
    st = list()
    
    for c in s:
        if c == '(':
            st.append(c)

        if c == ')':
            try:
                st.pop()
            except IndexError:
                return False

    return len(st) == 0