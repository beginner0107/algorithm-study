# https://www.acmicpc.net/problem/1316

"""
문제
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

출력
첫째 줄에 그룹 단어의 개수를 출력한다.

예제 입력
3
happy
new
year
예제 출력
3
"""

import sys; input=sys.stdin.readline


# 그룹 단어 세는 변수 초기화
count = 0
n = int(input())

for i in range(n):
    # 반복 돌면서 바로 전단계의 단어 저장할 변수 temp
    temp = ""
    # 중복 확인을 위한 set 자료형 letters
    letters = set()

    # n 번 반복해서 받을 인풋 값 word
    word = input()
    count += 1 # 일단 count + 1

    # 단어 반복 돌기
    for letter in word:
        # 그룹 단어가 아닌 경우 -1 하기
        if temp != letter and letter in letters:
            count -= 1
            break
        else:
            temp = letter
            letters.add(letter)

print(count)