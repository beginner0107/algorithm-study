# https://www.acmicpc.net/problem/1991

"""
이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.

예를 들어 위와 같은 이진 트리가 입력되면,

전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
가 된다.

입력
첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현한다.

출력
첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.

예제 입력 1
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .

예제 출력 1
ABDCEFG
DBAECFG
DBEGFCA
"""


import sys; input=sys.stdin.readline

n = int(input())
tree = {}

for _ in range(n):
    start, left, right = input().split()
    tree[start] = (left, right)


# 1. 전위 순회 : (루트) > (왼쪽 자식) > (오른쪽 자식) 탐색
def preorder(root):
    if root != '.':
        print(root, end='')  # root
        preorder(tree[root][0])  # left -> root
        preorder(tree[root][1])  # right -> root


# 2. 중위 순회 : (왼쪽 자식) (루트) (오른쪽 자식) 탐색
def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])


# 3. 후위 순회 : (왼쪽 자식) (오른쪽 자식) (루트) 탐색
def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')