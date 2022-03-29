'''
5. 온도변환 프로그램
- 온도를 입력받아 화씨나 섭씨로 변환하는 프로그램
 Enter a temperature: 20
 Convert to (F)ahrenheit or (C)elsius? F
 20 C = 68 F

 - 온도 변환공식
 Tc=(5/9)*(Tf-32)
 Tf=(9/5)*Tc+32
'''

temp = int(input("Enter a temperature: "))
conv = input("Convert to (F)ahrenheit or (C)elsius? ")
conv = conv.upper()

result = 0

if conv == 'F':
    result = (temp * 9 / 5) + 32
    print("{} C = {} F".format(temp, result))
elif conv == 'C':
    result = (temp - 32) * 5 / 9
    print("{} F = {} C".format(temp, result))
else:
    print("{} 는 잘못된 입력입니다" % conv)
