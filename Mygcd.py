def mygcd(a,b):
    i=min(a,b)
    while True:
        if a%i==0 and b%i==0:
            return i
        i=i-1
print(mygcd(12,3))

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
print(gcd(12,3))
