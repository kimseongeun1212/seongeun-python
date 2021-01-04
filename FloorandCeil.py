def fx(a):
    y=2*a + 0.7
    return y

def gx(a):
    y=4*a+0.3
    return y

ans1=fx(gx(2))
ans2=gx(fx(2))

print("f(x)ºg(x)=f(g(x))=2(4x+0.3)+0.7=", ans1,"(x=2 일때)")
print("g(x)ºf(x)=g(f(x))=4(2x+0.7)+0.3=", ans2,"(x=2 일때)")

print("바닥함수:", math.floor(ans1));
print("천정함수:", math.ceil(ans2));
