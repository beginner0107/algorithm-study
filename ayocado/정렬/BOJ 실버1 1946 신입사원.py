import sys
T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    applicant = [0]*n
    for j in range(n):
        paper, interview = map(int, sys.stdin.readline().split())
        applicant[j] = [paper, interview]

    applicant_sorted = sorted(applicant, key=lambda x: x[0])
    hired = 1
    man = applicant_sorted[0][1]
    for j in range(1, n):
        if applicant_sorted[j][1] < man:
            man = applicant_sorted[j][1]
            hired += 1

    print(hired)