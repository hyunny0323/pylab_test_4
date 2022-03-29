'''
8. 크기가 같은 두 리스트의 각 원소들을 곱하여 합
을 구하는 함수 listProd(a, b)를 만드시오. 이 함수를
이용하여 두 리스트의 곱을 출력하는 프로그램을 작
성하시오. 예) 인수가 a=[1, 0, 1], b=[1, 1, 2] 이라면
 3을 반환 (1*1 + 0*1 + 1*2 = 3)
'''


def list_prod(li1, li2):
    count = 0
    result = 0

    while True:
        result += li1[count] * li2[count]
        count += 1
        if count == len(li1):
            break

    return result


a = [1, 0, 1]
b = [1, 1, 2]

print(list_prod(a, b))
