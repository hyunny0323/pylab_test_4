'''
6. 반지름을 입력받아 구의 겉면적과 부피를 출력하
는 프로그램을 작성하시오.
'''
import math

r = int(input("구의 반지름을 입력해주세요 : "))

su_area = 4 * math.pi * r ** 2
volume = (4 / 3) * math.pi * r ** 3

print("반지름 {}, 구의 겉면적은 {:.2f}, 부피는 {:.2f} 입니다.".format(r, su_area, volume))
