# 테트로미노들
def T1(x, y) :
    if x > n-3 or y > m-2 :
        return 0
    else :
        return f[x][y] + f[x][y+1] + f[x+1][y+1] + f[x+2][y+1]

def T2(x, y) :
    if x > n-2 or y < 2:
        return 0
    else :
        return f[x][y] + f[x+1][y] + f[x+1][y-1]+f[x+1][y-2]

def T3(x,y) :
    if x>n-3 or y>m-2 :
        return 0
    else :
        return f[x][y] + f[x+1][y] + f[x+2][y] + f[x+2][y+1]
def T4(x,y) :
    if x>n-2 or y>m-3 :
        return 0
    else :
        return f[x][y] + f[x+1][y] + f[x][y+1] + f[x][y+2]

def A1(x,y) :
    if x > n-2 or y > m-2 :
        return 0
    else :
        return f[x][y] + f[x+1][y] + f[x+1][y+1] + f[x][y+1]

def B1(x,y) :
    if y> n-4 :
        return 0
    else :
        return f[x][y] + f[x][y+1] + f[x][y+2] + f[x][y+3]

def B2(x, y) :
    if x>n-4 :
        return 0
    else :
        return f[x][y] + f[x+1][y] + f[x+2][y] + f[x+3][y]

def C1(x,y) :
    if x> n-2 or x<1 or y>m-2 :
        return 0
    else :
        return f[x][y] + f[x+1][y] + f[x+1][y+1] + f[x+1][y-1]

def C2(x,y) :
    if x>n-3 or y>m-2 :
        return 0
    else :
        return f[x][y] + f[x+1][y] + f[x+1][y+1] + f[x+2][y]

def C3(x,y) :
    if x>n-2 or x<1 or y>m-2 :
        return 0
    else :
        return f[x][y] + f[x+1][y] + f[x][y-1] + f[x][y+1]

def C4(x,y) :
    if x>n-3 or y<1:
        return 0
    else :
        return f[x][y] + f[x+1][y] + f[x+2][y] + f[x+1][y-1]

def Z1(x,y) :
    if x>n-2 or y>m-3 :
        return 0
    else :
        return f[x][y] + f[x][y+1] + f[x+1][y+1] + f[x+1][y+2]

def Z2(x,y) :
    if x>n-3 or y<1:
        return 0
    else :
        return f[x][y] + f[x+1][y] + f[x+1][y-1] + f[x+2][y-1]

def Z3(x,y) :
    if x>n-2 or y < 2 :
        return 0
    else :
        return f[x][y] + f[x+1][y-1] + f[x][y-1] + f[x+1][y-2]

def Z4(x,y) :
    if x>n-3 or y>m-2:
        return 0
    else :
        return f[x][y] + f[x+1][y] + f[x+1][y+1] + f[x+2][y+1]

def R1(x,y) :
    if x>n-3 or y>m-2:
        return 0
    else :
        return f[x][y] + f[x+1][y] + f[x+2][y] + f[x][y+1]

def R2(x,y) :
    if x>n-2 or y>m-3:
        return 0
    else :
        return f[x][y] + f[x+1][y+2] + f[x][y+1]+ f[x][y+2]

def R3(x,y) :
    if x>n-3 or y<1 :
        return 0
    else :
        return f[x][y] + f[x+1][y] + f[x+2][y] + f[x+2][y-1]

def R4(x,y) :
    if x>n-2 or y>m-3 :
        return 0
    else :
        return f[x][y] + f[x+1][y] + f[x+1][y+1] + f[x+1][y+2]
    
# 종이에 쓰인 수
f = []

n, m = map(int, input().split())

# 배열 입력
for i in range(n) :
    f.append(list(map(int, input().split())))

MAX = 0
sig = []

for i in range(n) :
    for j in range(m) :
        res = max(T1(i,j), T2(i,j), T3(i,j), T4(i,j), A1(i,j), R1(i,j),
                  R2(i,j), R3(i,j), R4(i,j), B1(i,j), B2(i,j), C1(i,j),
                  C2(i,j), C3(i,j), C4(i,j), Z1(i,j), Z2(i,j), Z3(i,j),
                  Z4(i,j))
        if res > MAX :
            MAX = res


print(max(sig))

