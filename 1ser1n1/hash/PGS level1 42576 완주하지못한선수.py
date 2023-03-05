def solution(participant, completion):
    sumHash = 0
    hashDict = {}
    
    # Participant의 dictionary 만들기 / key = 해시값, value = 참가자 이름
    # Participant의 sum(hash) 구하기
    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)
    
    # completion의 선수를 sumhash에서 빼기
    for comp in completion:
        sumHash -= hash(comp)
    
    # 남은 값이 완주하지 못한 선수의 해시값이 된다
    return hashDict[sumHash]
