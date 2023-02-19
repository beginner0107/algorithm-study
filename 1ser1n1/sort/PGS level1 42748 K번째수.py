import copy

def solution(array, commands):
	answer = []
	for s in commands:
		split_a = sorted(copy.deepcopy(array[s[0]-1:s[1]]))
		answer.append(split_a[s[2]-1])
	return answer

