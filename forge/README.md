# 代码思路
ECDSA签名与验证：   
KeyGen: P=dG, n is order
Sign(m)：   
k=Zn*,R= kG    
r=Rxmodn,r!=0    
e = hash(m)   
s =k^(-1)(e + dr) mod n    
Signature is (r,s)    
Verify (r,s) of m with P：   
e = hash(m)   
W=s^(-1)modn    
(r',s')=e·wG +r·wP    
Check if r' == r    
Holds for correct sig since   
es^(-1)G +rs^(-1)P= s^(-1)(eG +rP) = k(e+ dr)^(-1)(e +dr)G = kG = R

Shnnor签名与验证：    
Key Generation
P=dG    
Sign on given message M   
randomly k, let R = kG   
e = hash(R||M)    
s = k+edmod n   
Signature is: (R,s)   
Verify (R,s) of м with P    
Check sG vs R+eР    
sG =(k+ed)G = kG +edG = R+eP   

伪造签名通过验证：  
A= (r,s) is valid signature of m with secret key d.   
If only the hash of the signed message is required.     
Then anyone can forge signature A'=(r' ,s') for d   
(Anyone can pretend to be someone else)   
Ecdsa verification is to verify:    
s^(-1)(eG+rP)= (x ,y')= R',r'= x'mod n == r ?.   
To forge, choose u,v ∈Fn    
Compute R'= (x',y') = uG +vP    
Choose r'= x' mod n, to pass verification, we need. s'^(-1)(e'G+r'P)= uG+ vP    
s'^(-1)e' = u mod n =>e'= r'uv^(-1)mod n.     
s'^(-1)r' = v mod n => s'= r'v^(-1) mod n   
A'=(r' ,s') is a valid signature of e' with secret key d   

定义椭圆曲线上的乘法运算为elliptic_multiply，椭圆曲线上的同一点加法运算（*2运算）为elliptic_double，椭圆曲线上的不同点加法运算为elliptic_add。generate_key生成公私钥对，sign函数进行签名，verify函数进行验证，verify1函数在已知e而不知道m的情况下进行验证。forge函数进行伪装。

参数设置如下：
![image](https://user-images.githubusercontent.com/105595347/181921163-f34da2b5-fc0f-4c89-bbb4-75760dccb67d.png)

# 运行指导
在idel上运行
# 运行截图
![image](https://user-images.githubusercontent.com/105595347/181871690-9fd02822-ddc7-404a-9851-f1260fc6d310.png)

# 贡献
个人独立完成
