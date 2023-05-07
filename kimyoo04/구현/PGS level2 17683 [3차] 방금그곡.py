# https://school.programmers.co.kr/learn/courses/30/lessons/17683

"""
핵심
- 시간 계산으로 분으로 통일
- 정규식을 통한 소문자 문자열 치환
- 재생 시간 내림차순 정렬
"""

import re

# 1. 시간을 분으로 통일
def convert_minutes(start, end):
    start = start.split(':')
    end = end.split(':')
    start = int(start[0]) * 60 + int(start[1])
    end = int(end[0]) * 60 + int(end[1])
    return end - start

# 2. # 글자 처리 처리
def sharp_change(music):
    music = re.sub('C#', 'c', music)
    music = re.sub('D#', 'd', music)
    music = re.sub('F#', 'f', music)
    music = re.sub('G#', 'g', music)
    music = re.sub('A#', 'a', music)
    return music

def solution(m, musicinfos):
    # 네오가 기억한 멜로디
    m = sharp_change(m)

    # 정답 배열
    answer = []

    # musicinfos를 순회하며 m이 포함되는지 확인
    for musicinfo in musicinfos:
        # 시간, 제목, 멜로디
        musicinfo = musicinfo.split(',')
        # 재생 시간
        time = convert_minutes(musicinfo[0], musicinfo[1])

        music = sharp_change(musicinfo[3])
        # 재생된 멜로디 (재생 시간만큼 반복) -> 재생 시간이 긴 음악이 먼저 오도록 하기 위함
        music = music * (time // len(music)) + music[:time % len(music)]

        # m이 포함되는지 확인
        if m in music:
            # [음악 제목, 재생 시간] 추가
            answer.append([musicinfo[2], time])

    # 포함되는 음악이 없다면 (None) 반환
    if not answer:
        return '(None)'
    # 재생 시간이 긴 순서대로 내림차순 정렬
    answer.sort(key=lambda x: -x[1])
    # 재생 시간이 같다면 먼저 입력된 순서대로 정렬
    return answer[0][0]

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])) # "HELLO"
# print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])) # "FOO"
# print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])) # "WORLD"
