try:
    fileName = input('로딩할 파일의 이름을 입력 하세요 : ')
    fileName = fileName + '.txt'
    file = open(fileName, 'rt')
except FileNotFoundError:
    print(fileName + '는 없는 파일 입니다 !')
else:
    print(fileName + '를 읽었습니다.')
    answer = file.read()
    file.close()
    answer = int(answer)  # 정답
    cnt = 0  # 시도 횟수
    L = 1  # 시작 수
    H = 100  # 끝 수
    while True:
        try:
            #   사용자가 입력 하는 숫자
            num = int(input(str(L) + ' ~ ' + str(H) + ' : '))
        except ValueError:
            print('정수가 아닙니다. 다시 입력 하세요 !')
            continue
        if num < L or H < num:
            print(str(L) + '~' + str(H) + '이 아닙니다. 다시 입력 하세요 !')
            continue
        cnt += 1
        if num == answer:
            print(str(answer) + ' 정답 입니다 ! :D')
            break
        elif num < answer:
            print('UP !')
            L = num + 1
        else:
            print('DOWN !')
            H = num - 1

    with open(fileName, 'wt') as file:
        file.write(str(cnt) + '번만에 정답을 맞추셨습니다 ! :D')
