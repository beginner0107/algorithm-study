# 이진트리의 노드수는 깊이를 d라고 하면, 시그마(2^n) (n=0~d-1)
# 1. 주어진 숫자를 이진수로 바꾸고, 앞에 0을 붙여서 이진트리의 길이와 같게 만들 수 있는지 확인
# (뒤에 0이 붙으면 자리수가 달라져버리므로, 앞에 0도 하나만 붙일 수 있음)
# 앞에 0을 무한정 붙일 수는 없음 (이진트리여야 하므로)
# 2. 각 부모노드들이 1이 맞는지 확인
# 개수를 맞췄을 때, 중앙값이 최상위 노드임. 양쪽을 계속 확인하면 됨.
# (부모노드가 0이면, 만들 수 없음)
# 64 32 16 8 4 2 1
# 58 -> 111010 -> 0111010 
#    1
#  1   1
# 0 1 0 0
# 7: 111, 42: 101010
# 42 -> 101010 -> 0101010
#    1
#  1   1
# 0 0 0 0
# 5: 101 -> 부모노드가 0이 될 수 없으므로 만들 수 없음. 앞에 0 붙여도 만들 수 X

from math import log2

def is_tree(num_bin, prev_parent):
    
    # 중앙값(자손) 기준으로 재귀적으로 확인
    mid = len(num_bin) // 2
    if num_bin:   # 자식이 더 존재할 때,
        child = (num_bin[mid] == '1')   # '1'인 요소가 있는지 (더 뻗어나가야 하는지)
    else: 
        return True
    
    # 현재 리스트의 '1'인 자식이 존재하므로, 부모가 존재해야함.
    if child and not prev_parent:
        return False
    else:    # 자식의 양쪽 자식 노드들 재귀
        return is_tree(num_bin[mid + 1:], child) and is_tree(num_bin[:mid], child)

def solution(numbers):
    ans = []
    
    for n in numbers:
        # 1. 주어진 수를 이진수로 변환하기
        binn = bin(n)[2:]
        
        # 2. 포화 이진 트리의 노드 수만큼 늘려주기
        tmp = int(log2(len(binn))) + 1
        digit = 2 ** tmp - 1
        binn = "0" * (digit - len(binn)) + binn
        
        # 3. 부모 노드가 '1'인지 확인
        if binn[len(binn) // 2] != '1':
            ans.append(0)
            continue
        
        # 4. 부모 노드의 자식 노드들을 재귀적으로 확인하며, 부모 노드가 '1'인지 확인
        if is_tree(binn, True):
            ans.append(1)
            continue
            
        ans.append(0)
    
    return ans