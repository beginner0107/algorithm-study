input_number = input()

input_list = list(map(int, list(input_number)))

input_list.sort(reverse=True)

for i in input_list:
    print(i, end='')
