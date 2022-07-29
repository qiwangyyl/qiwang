# 代码思路
ECDSA签名与验证：
KeyGen:P=dG,n is order
Sign(m)：   
k Z*,R= kG    
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
es-1G +rs-1P= s-1(eG +rP) = k(e+ dr)-1(e +dr)G = kG = R   
