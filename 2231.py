def gongyaksu(a,b):
    k = min(a,b)
    while True:
        if (a%k==0 and b%k==0):
            return k
        k -= 1
def gongbaesu(a,b):
    k = max(a,b)
    while True:
        if (k%a==0 and k%b==0):
            return k
        k += 1

m,n = map(int,input().split())
print(gongyaksu(m,n))
print(gongbaesu(m,n))