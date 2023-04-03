n = int(input())

s = [0, 1, 1]
for i in range(3, n+1):
  s.append(s[i - 2] + s[i - 1])
print(s[n])