def solution(files):
    num = {str(i): 0 for i in range(10)}
    answer = []
    file_list = []
    for file in files:
        file_list.append(File(file, num))
    file_list.sort(key=lambda x: (x.head, x.number))
    for f in file_list:
        answer.append(f.filename)
    return answer


class File:
    def __init__(self, filename, num):
        self.filename = filename
        self.head = ''
        self.number = -1
        self.tail = ''
        self.parse_file_name(num)

    def parse_file_name(self, num):
        head_index = -1
        number_index = len(self.filename)
        is_start = False
        for i in range(len(self.filename)):
            if self.filename[i] in num and not is_start:
                head_index = i
                is_start = True
            elif self.filename[i] not in num and is_start:
                number_index = i
                break
        self.head = self.filename[:head_index].upper()
        self.number = int(self.filename[head_index:number_index])
        self.tail = self.filename[number_index:]

    def __str__(self):
        return f'{self.head}, {self.number}, {self.tail}'
