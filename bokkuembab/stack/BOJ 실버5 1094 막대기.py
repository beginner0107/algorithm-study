goal = int(input())       # 막대기의 목표 길이

# 막대를 잘라 => 64 -> 32 32 -> 32 16 16 -> 32 16 8 8 -> 32 16 8 4 4
st = []   # 막대의 길이를 저장하고 있는 스택
st.append(64)       # 처음 막대의 길이 저장

while sum(st) != goal:      # 합이 목표에 도달할 때까지 반복
    tmp = st.pop() // 2     # 막대기 하나 꺼내서 반으로 분할 (마지막에 넣은 것이 분할한 막대기)
    st.append(tmp)          # 분할한 막대기 일단 하나 넣기
    
    if sum(st) < goal:      # 하나만 넣었을 때, 목표보다 작으면 하나 더 넣기
        st.append(tmp)
    
print(len(st))