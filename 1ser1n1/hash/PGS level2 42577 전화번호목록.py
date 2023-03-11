def solution(phone_book):
    phoneBook = sorted(phone_book) #정렬시 접두사 별로 길이가 짧은 것 부터 정렬됨
    
    for p1, p2 in zip(phoneBook, phoneBook[1:]): #zip함수를 이용하여 리스트 2개를 반복 순환
        if p2.startswith(p1): #p2문자열 접두사가 p1이면 true
            return False
    return True