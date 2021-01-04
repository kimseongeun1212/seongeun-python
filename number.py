#01

#정수형 상수: -10, 0, 10 같은 정수
intNumber1 = 10;

#실수형 상수: -0.5, 2.5과 같이 분수로 표현가능한 유리수, 무리수를 포함하는 실수
floatNumber2 = 3.14; #실수선언
floatNumber3 = 3/4; #실수선언
floatNumber4 = 1.25e4 #실수선언
floatNumber5 = -0.5e3 #실수선언

#복소수형 상수: 실수부+허수로로 되어 있는 복소수
complexNumber6 = 1+5j;  #복소수 선언
complexNumber7 = complex(2,-4); #복소수 선언

print("intNumber1 = %d" %intNumber1);

print("floatNumber2 = %f" %floatNumber2);
print("floatNumber3 = %f" %floatNumber3);
print("floatNumber4 = %f" %floatNumber4);
print("floatNumber5 = %f" %floatNumber5);

print("complexNumber6 = {0}".format(complexNumber6));
print("complexNumber6.real = {0}".format(complexNumber6.real));
print("complexNumber6.imag = {0}".format(complexNumber6.imag));
print("complexNumber7 = {0}".format(complexNumber7));

#02

a=2
b=3

hap = a+b #더하기
cha = a-b; #빼기
gop = a*b; #곱셈
nap = a/b; #나눗셈

seung = a**b #제곱

print("hap = %d"%hap);
print("cha = %d"%cha);
print("gop = %f"%gop);
print("nap = %f"%nap);
print("seung = %d"%seung);

#03
#10진수 상수
intNumber1 = 2;

#2진수 상수
binNumber2 = 0b11;

#8진수 상수
octNumber3 = 0o12;

#16진수 상수
hexNumber4 = 0x14;

print("intNumber1 = %d" %intNumber1);
print("binNumber2 = %d" %binNumber2);
print("octNumber3 = %d" %octNumber3);
print("hexNumber4 = %d" %hexNumber4);
print("===========================");

#2진수를 10진수로 변환
bin = 0b1000
print(int(bin))

#8진수를 10진수로 변환
oct = 0o320
print(int(oct))

#16진수를 10진수로 변환
hex = 0xf0
print(int(hex))

#10진수를 2진수로 변환
intNum=100;
print("{:#b}".format(intNum))

#10진수를 8진수로 변환
print("{:#o}".format(intNum))

#10진수를 16진수로 변환
print("{:#x}".format(intNum))
