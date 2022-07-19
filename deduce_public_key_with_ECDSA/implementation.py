from gmssl import sm3,func
from hashlib import sha256
import secrets
from Crypto.Util import number
A = 115792089210356248756420345214020892766250353991924191454421193933289684991996
B = 18505919022281880113072981827955639221458448578012075254857346196103069175443
G_X = 22963146547237050559479531362550074578802567295341616970375194840604139615431
G_Y = 85132369209828568825618990617112496413088388631904505083283536607588877201568
G = (G_X, G_Y)#G为基点
# 有限域的阶
P = 115792089210356248756420345214020892766250353991924191454421193933289684991999
# 椭圆曲线的阶
N = 115792089210356248756420345214020892766061623724957744567843809356293439045923
#椭圆曲线上的不同点加法运算
def elliptic_add(p,q):
    if p==0 and q==0:return 0
    elif p==0:return q
    elif q==0:return p
    else:
        #保证p[0]<=q[0]
        if p[0]>q[0]:
            temp=p
            p=q
            q=temp
        r=[]
        #当P！=Q时，两点纵坐标相减的值与横坐标相减的值相除就是直线的斜率
        slope=(q[1]-p[1])*number.inverse(q[0]-p[0],P)%P
        r.append((slope**2-p[0]-q[0])%P)
        r.append((slope*(p[0]-r[0])-p[1])%P)
        return (r[0],r[1])
#椭圆曲线上的同一点加法运算（*2运算）
def elliptic_double(p):
    #当P=Q，计算过P(Q)点切线的斜率为椭圆曲线公式两边求导相除：λ = (3*p[0]² + A)/2*p[1]
    r=[]
    slope=(3*(p[0]**2) + A)*number.inverse(2*p[1],P)%P
    r.append((slope**2-2*p[0])%P)
    r.append((slope*(p[0]-r[0])-p[1])%P)
    return (r[0],r[1])
#椭圆曲线上的乘法运算
def elliptic_multiply(s,p):
    n=p
    r=0#无穷远点
    s_bin=bin(s)[2:]#转化为二进制
    s_len=len(s_bin)#二进制长度
    for i in reversed(range(s_len)):#从s_len-1到0逐位计算
        if s_bin[i]=='1':
            r=elliptic_add(r,n)
        n=elliptic_double(n)#n乘2,继续循环
    return r
#生成公私钥    
def generate_key():
    #私钥：大整数
    #公钥：椭圆曲线上的点,有基点和私钥生成
    prikey=int(secrets.token_hex(32),16)#返回十六进制随机文本字符串,有n个字节的随机字节，每个字节转换为两个十六进制数字
    pubkey=elliptic_multiply(prikey,G)
    return prikey,pubkey

#签名生成（r,s）
def sign(private_key,mes):
    e=hash(mes)
    print("e",e)
    k=secrets.randbelow(P)#0-P的随机数
    point1=elliptic_multiply(k,G)#该点为k*G
    print("生成的椭圆曲线上的点：",point1)
    r=point1[0]%P
    #计算s=((k)^(-1)⋅(e+r⋅private_key))mod n
    s=(number.inverse(k,N)*(e+r*private_key))%N
    return (r,s)
'''计算二次剩余x^2=y(mod p)'''
def QR(y,p):
    if pow(y,(p-1)//2,p)!=1:
        return
    if p%4==3:
        return pow(y,(p+1)//4,p)
    #计算p-1=(2^s)*q
    q=p-1
    s=0
    while q%2==0:
        q=q//2
        s+=1
    r=pow(y,(q+1)//2,p)
    r0=pow(y,q,p)
    for z in range(2,p):
        if pow(z,(p-1)//2,p)==p-1:
            c=pow(z,q,p)
            break
    #找到p的一个二次非剩余z，计算c为z^q%p
    m=s
    if r0==1:
        return r#如果y^q==1则r=x
    i=0
    while r0!=1:#利用计算出的y^q，计算其二次方是否为1%p,若不是则乘c^(2^(m-i-1))继续判断其二次方
        temp=pow(r0,2**(i+1),p)
        i+=1
        if temp%p==1:
            b=pow(c,2**(m-i-1),p)#b=c^(2^(m-i-1))%p
            r=r*b%p
            c=b*b%p
            r0=r0*c%p#计算r的二次方
            m=i
            i=0
    return r
'''根据签名内容反推公钥'''
def deduce_public_key(sig,mes):
    r=sig[0]
    s=sig[1]
    x=r%P
    y2=((x**3)+A*x+B)#y^2=x^3+Ax+B
    y=QR(y2,P)
    print('y',y)
    point1=(x,y)
    point2=(x,P-y)#可能计算出y或-y
    e=hash(mes)
    print("e",e)
    eG=elliptic_multiply(e%N,G)
    fu_eG=(eG[0],P-eG[1])#计算-e[G]
    skG1=elliptic_multiply(s%N,point1)
    sk_eG1=elliptic_add(skG1,fu_eG)#(sk-e)[G]即为rd[G]
    d1=elliptic_multiply(number.inverse(r,N),sk_eG1)
    skG2=elliptic_multiply(s%N,point2)
    sk_eG2=elliptic_add(skG2,fu_eG)#(sk-e)[G]即为rd[G]
    d2=elliptic_multiply(number.inverse(r,N),sk_eG2)
    return d1,d2
    
    
private_key,public_key=generate_key()
print("真实公钥：",public_key)
mes="qiwang"
sig=sign(private_key,mes)
print("签名：",sig)
pub1,pub2=deduce_public_key(sig,mes)
print('推测公钥为：',pub1,"或",pub2)
