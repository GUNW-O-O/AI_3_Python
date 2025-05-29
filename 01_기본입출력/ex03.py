# input() : 입력 함수
A = input("A : ")
B = input("B : ")
C = int(input("C : "))

# input 함수는 값을 입력받아 문자열(str) 로 가져온다

print("A + B : " + (A + B))

A = int(A)
B = int(B)
print("A + B : ",(A + B), sep="")
print("A + B + C :",(A + B + C), sep="")