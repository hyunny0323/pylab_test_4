'''
3. 1 ~ n 까지의 곱인 n! = 1*2*3*...*n을 구하는 함
수 factorial(n)을 만드시오. 사용자로부터 n값을 입력
받고 이 함수를 이용하여 n! 값을 출력하는 프로그램
을 작성하시오.
'''

n = int(input("자연수 N을 입력해주세요 : "))

result = 1

for i in range(1, n + 1):
    result *= i

print(result)
