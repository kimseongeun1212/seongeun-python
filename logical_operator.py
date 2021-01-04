#논리 연산자를 쓰기 위해 operator를 import 해즈고 시작
import operator

bool1 = [True];
bool2 = [True,False];
bool3 = [False];
bool4 = [True,False];

#논리연산자 AND
print("=====논리연산자 AND=====")
for x in bool1:
    for y in bool2:
        print(x and y);

      
for x in bool3:
    for y in bool4:
        print(x and y);

#논리연산자 OR
print("=====논리연산자 OR=====")
for x in bool1:
    for y in bool2:
        print(x or y);
        
      
for x in bool3:
    for y in bool4:
        print(x or y);
        

#논리연산자 XOR
print("=====논리연산자 XOR=====")
for x in bool1:
    for y in bool2:
        print(operator.xor(x,y))
        
for x in bool3:
    for y in bool4:
        print(operator.xor(x,y))
