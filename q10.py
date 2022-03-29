'''
10. 곱셉 문제 출제 프로그램 - 한자리 수 곱셈문제(예 1*3, 7*6)를 제시하고 답을
평가하는 프로그램을 작성하시오. - 사용자에게 임의의 두 숫자를 제시하고, 답을 입력
받아 맞았는지 틀렸는지 알려줌. - 사용자에게 계속 여부를 물어보고 멈추기를 원하
면 정답률을 %로 알려주고 종료. - 난수발생은 함수 randint() 함수사용
 # 1~9 사이의 난수 생성
 n1 = randint(1, 9)
'''

import random

count = 0
correct = 0

print("<곱셉 문제 프로그램 / n * m 의 값을 입력하시오 / 종료하려면 -1을 입력하시오>")

while True:
    n1 = random.randint(1, 9)
    n2 = random.randint(1, 9)
    answer = n1 * n2

    result = int(input("{} * {} = ".format(n1, n2)))

    if result == answer:
        count += 1
        correct += 1
        print("\t정답 / 푼 문제 수 : {} / 정답률 : {:.2f}%".format(count, (correct/count) * 100))
    elif result == -1:
        print("\t종료되었습니다. / 푼 문제 수 : {} / 정답률 : {:.2f}%".format(count, (correct / count) * 100))
        break
    else:
        count += 1
        print("\t오답 / 푼 문제 수 : {} / 정답률 : {:.2f}%".format(count, (correct / count) * 100))


