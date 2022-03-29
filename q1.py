'''
1. 자연수 N을 입력받아 1 ~ N 사이의 수의 합을 구하여 출력하는 프로그램을 작성하시오.
'''

n = int(input("자연수 N을 입력해주세요 : "))

result = 0

for i in range(n):
    result += i

print(result)
