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

