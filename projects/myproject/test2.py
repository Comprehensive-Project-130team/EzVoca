print("안녕하세요")
'''->주석 처리하는 법
여러 줄의
주석을
처리하는
방법입니다
'''
'''
a=10
b=20
print('a는 =', a)
print('b는 =', b)
print('a ' '+' ' b' ' =' ,(a+b))
'''
'''name = input('이름을 입력해주세요.')'''

#a = '8'
#b = '16'
#print(a+b)#문자 + 정수 계산 안됨
         #문자 + 문자 하면 문자끼리 붙어져서 출력됨
'''         
a=int(input('a 입력 : '))
b=int(input('b 입력 : '))
c=int(input('c 입력 : '))

print(a,b,c,a+b+c)
'''
'''
def 더하기(a, b):
    c = a + b
    return c
print('함수의 샐행값은 : ', 더하기(4, 5))
print(더하기(4, 5) + 4)
'''
class JSS:
    def __init__(self):
        self.name = str(input("이름 : "))
        self.age = int(input("나이 : "))
    def show(self):
        print("나의 이름은 {}, 나이는 {}세입니다.".format(self.name, self.age))
a = JSS()
a.name
a.age
a.show()

