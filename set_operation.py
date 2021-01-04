#01

s1 = set([1,3,5,7,9,10])
s2 = set([1,2,4,6,8,10])

#집합
print("s1 = ",s1)
print("s2 = ",s2)

#집합의 기수
print("s1 집합의 기수: ", len(s1))
print("s2 집합의 기수: ", len(s2))

print("=======================")

#합집합
union1 = s1 | s2
union2 = s1.union(s2)
print("합집합: ",union1)
print("합집합: ",union2)
print("합집합의 기수: ", len(union1))


#교집합
inter1 = s1 & s2
inter2 = s1.intersection(s2)
print("교집합: ",inter1)
print("교집합: ",inter2)
print("교집합의 기수: ", len(inter1))

#차집합
differ1 = s1 - s2
differ2 = s1.difference(s2)
print("차집합: ",differ1)
print("차집합: ",differ2)
print("차집합의 기수: ", len(differ1))
print("=======================")

# 부분집합 확인
subs = s1.issubset(s2)
print("s1은 s2 부분집합인가요 ",subs)
# 확대집합 확인
sups = s1.issuperset(s2)
print("s1은 s2 상위(초)집합인가요 ",sups)



#02
seta={2,4,6,8,10,12,14,16,18,20}
setb={2,5,10,15,20}

val=4
if val in seta:
    print(val,"은 집합 A에 원소이다")
else:
    print(val,"은 집합 A에 원소가 아니다")

val=2
if val in seta and setb:
    print(val,"은 집합 A와 집합 B에 원소이다")
else:
    print(val,"은 집합 A와 집합 B에 원소가 아니다")


val=5
if val in seta or setb:
    print(val,"은 집합 A또는 집합B에 원소이다")
else:
    print(val,"은 집합 A또는 집합B에 원소가 아니다")

print("집합 A는 집합B의 부분집합이다:",setb <= seta)
print("집합 A는 집합B의 진성부분집합이다:",setb < seta)
print("집합 A는 집합B의 포함집합이다:",setb <= setb)
print("집합 A는 집합B의 진성포함집합이다:",setb < seta)
