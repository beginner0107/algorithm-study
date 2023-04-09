n = int(input())
# 제공된 값을 저장
bug = [1,2,4,7]

# 분열 후 소멸, 짝수의 경우 4일째, 홀수의 경우 3일째이므로 값을 더함
for i in range(4,21) :
    if i%2==0 :
        bug.append(bug[i-4]+bug[i-3]+bug[i-2]+bug[i-1])

    else :
        bug.append(bug[i-3]+bug[i-2]+bug[i-1])

print(bug[n-1])
