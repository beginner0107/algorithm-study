def solution(m, musicinfos):
    # 정답이 들어갈 수 있는 배열
    answer = []
    # 한번 거른 순서쌍들
    mi = []
    # 순서용 수
    cnt = 0
    for info in musicinfos :
        t = info.split(',')
        t[3] = t[3].replace('C#', 'c')
        t[3] = t[3].replace('D#', 'd')
        t[3] = t[3].replace('F#', 'f')
        t[3] = t[3].replace('G#', 'g')
        t[3] = t[3].replace('A#', 'a')
        # 시간 계산
        hour = (int(t[1][0:2]) - int(t[0][0:2]))
        time = (int(t[1][3:5]) - int(t[0][3:5]))
        if time < 0 :
            hour = hour - 1
            time = time + 60
        if hour < 0 :
            hour = hour + 24
        playtime = hour * 60 + time
        l = len(t[3])
        wholen = (playtime // l) + 1
        music = (t[3] * wholen)[0:playtime]
        mi.append([playtime, t[2], music, cnt])
        cnt = cnt + 1
        
    for i in range(len(mi)) :
        m = m.replace('C#', 'c')
        m = m.replace('D#', 'd')
        m = m.replace('F#', 'f')
        m = m.replace('G#', 'g')
        m = m.replace('A#', 'a')
        # 조건 만족하면 답 후보 배열에 넣음
        if m in mi[i][2] :
            answer.append(mi[i])
        # 플레이 시간은 내림차로, 입력 순서는 오름차로 저장
    answer.sort(key=lambda x: (-x[0], x[3]))
    if len(answer) == 0:
        return "(None)"
    return answer[0][1]
