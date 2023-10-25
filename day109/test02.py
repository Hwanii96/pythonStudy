# 실습 문제
"""
test.txt에 정수 1개가 입력된 상황
읽어 들일 파일의 이름을 입력 >> apple
test.txt 를 읽었습니다.
apple.txt 는 없는 파일 입니다 !

1 ~ 100 >> 50
DOWN !
1 ~ 49 >> 25
UP !
26 ~ 49 >> 32
32 ! 정답입니다 ! :D
text.txt
3번만에 정답을 맞추셨습니다. :D

1 ~ 100 >> 500

1 ~ 100 의 범위를 초과 했습니다. 다시 입력해주세요 !
(범위를 벗어난 숫자를 입력 하면 카운트 에는 포함 되지 않음)

또한 정수 범위 예외 뿐만 아니라, 문자를 입력 해도 예외가 발생 하기 때문에,
그런 경우에도 정수가 아닙니다 ! 등으로 예외 처리 되도록 하기.
"""

import os  # 파일을 읽기 위해 os 모듈 import

with open('test.txt', 'wt') as file:
    num = int(input('정수 입력 : '))
    file.write(str(num))

with open('test.txt', 'rt') as file:
    textFile = file.read()
    print(textFile)

print('예시 : test.txt')
fileName = input('파일 이름을 입력 하세요 : ')

if os.path.exists(fileName):
    print(fileName, '을 읽었습니다.')
else:
    print(f'{fileName} 은 없는 파일 입니다 !')

with open('test.txt', 'r') as file:  # r => read mode (파일 읽기만 가능한 모드)
    txtNumber = int(file.read())  # 메모장에서 숫자 읽어 오기

maxNum = 100  # 입력 가능한 최대값
minNum = 1  # 입력 가능한 최소값
cnt = 0  # 입력 횟수

while True:
    try:
        userInput = int(input("찾고자 하는 정수를 입력 하세요 : "))
        if userInput < minNum or userInput > maxNum:
            print('1 ~ 100의 범위를 초과 했습니다. 다시 입력해 주세요 !')
            continue
        elif userInput == txtNumber:  # 사용자가 입력한 값이 파일 안에 있을 때
            cnt += 1
            print(userInput, '! 정답 입니다 ! :D')
            print(cnt, '번 만에 정답을 맞추셨습니다. :D')
            break
        elif userInput > txtNumber:  # 사용자가 입력한 값이 파일 안에 정수 보다 클 경우
            print('DOWN !')
            cnt += 1
        elif userInput < txtNumber:  # 사용자가 입력한 값이 파일 안에 정수 보다 작을 경우
            print('UP !')
            cnt += 1
    except ValueError:
        print('정수만 입력 할 수 있습니다 !')
    except Exception:
        print('처리 할 수 없는 예외 입니다.')
