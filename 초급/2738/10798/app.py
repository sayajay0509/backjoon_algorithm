matrix = [input() for _ in range(5)]  # 최대 5개의 문자열 입력
output = ''
for i in range(15):  # 최대 15자까지 있을 수 있으므로
    for string in matrix:
        if i < len(string):  # 해당 문자열의 길이가 i보다 큰 경우에만 접근
            output += string[i]

print(output)