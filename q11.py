'''
11. 파일 출력 프로그램
사용자가 요청한 파일을 읽어서 라인번호를 붙여 출
력하는 프로그램을 작성하시오. 사용자가 요청한 파
일이 없는 경우 크래시되지 않고 이를 알려주고 종
료되도록 하시오

파일: file.txt
    Opens a file for reading only in binary.
    The file pointer is placed.
    This is the default mode.

출력
1: Opens a file for reading only in binary.
2: The file pointer is placed.
3: This is the default mode. ...
'''
import sys

line_count = 0

filename = input("파일 이름을 입력하시오 : ")

try:
    f = open(filename, 'r')
except FileNotFoundError:
    print("존재하지 않는 파일입니다. / 종료되었습니다")
    sys.exit(0)
else:
    while True:
        line = f.readline()
        line_count += 1
        if not line:
            break
        print("{}: {}".format(line_count, line), end="")
