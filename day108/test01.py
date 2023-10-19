# C:\Users\dhfg0\PycharmProjects\pythonProject\day108\test01.py

# 파일 입출력
# 파일 객체 = open('파일명.확장자','모드')

# 별도의 경로를 입력 하지 않으면 현재 test01.py 파일이 존재하는 위치가 디폴트 경로가 된다.
# 절대 경로와 상대 경로를 모두 지원 한다.
# wt => writetext mode (파일 쓰기 모드)  / rt => readtext mode (파일 읽기 모드) / at => 파일 이어 쓰기 모드
file = open('test.txt', 'wt')
file.close()  # close() 메서드를 사용 해서 메모리 누수를 방지.

# with 문 => close() 메서드를 포함하는 문법 (실질적으로 많이 사용 되는 문법 이다)
# with open('파일명','모드') as 파일 객체:
#   pass

with open('test.txt', 'wt') as file:
    file.write('줄\n바꿈')

with open('test.txt', 'at') as file:
    file.write('\n 파일 이어 쓰기 "at" ')

with open('test.txt', 'wt') as file:
    while True:
        tmp = input('입력 : ')
        if not tmp:  # 파이썬은 동적 타이핑 언어로 자동 으로 null 체크를 한다. not 을 붙혀서 입력값이 없니 ? 그러면 break 해.
            break
        file.write(tmp + '\n')  # file.write() 는 자동 줄바꿈을 지원 하지 않아서 '\n' 으로 줄바꿈 처리 하기.

with open('test.txt', 'rt') as file:
    tmp = file.read()  # read() 만 작성 하면 해당 파일의 전체를 읽어 오는 메서드.
    print(tmp)
