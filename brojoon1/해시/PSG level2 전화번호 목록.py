def solution(phone_book):
    answer = True
    phone_hm = {}
    
    # key: 전화번호 / value: 임의의 값(0)
    for phone_number in phone_book:
        phone_hm[phone_number] = 0
        
    # 주어진 phone_book 리스트에 담긴 번호를 하나씩 본다.
    for phone_number in phone_book:
        str_num = ''
        
        # 그 번호를 한 글자씩 잘라서
        for i in phone_number:
            str_num += i
            
            # 자기 자신이면 continue
            if(str_num == phone_number):
                continue
            
            # 하나씩 자른 번호가 phone_hm에 있으면 answer = False
            if str_num in phone_hm:
                answer = False
            
    return answer