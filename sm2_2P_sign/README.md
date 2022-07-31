# 代码说明
该过程中的公钥Public key:     
P = [(d1d2)^(-1)]G    
Private key: d = (d1d2)^(-1) - 1

该过程中的签名过程Signature：   
(k1*k3 + kz)G = (x1,y1)   
r=(x1+e)modn    
s=(1+d)^(-1)*((k1*k3 + k2)-r.d) mod n   

签名方A：

(1) Generate sub private key d1 ∈ [1,n- 1] , compute P1 = d^(-1)*G    
发送P1

(3) Set Z to be identifier for both parties, message is M     
Compute M' = Z||M, e = Hash(M')   
Randomly generate k1 ∈ [1,n-1], compute Q1 = k1*G   
发送Q1，e

(5) 接受r,s2,s3   
Generate signature (r,s)       
Compute s = (d1*k1)*S2 +d1*S3-r mod n     
If s！=0 or s ！=n-r , output signature (r,s)    

对方B：    
(1) Generate sub private key d2∈[1,n- 1]

(2) Generate shared public key: compute P= d2^(-1)*P1-G     
publish public key P

(4) Generate partial signature r :    
Randomly generate k2∈[1,n - 1], compute Q2 =k2*G    
Randomly generate k3 ∈ [1,n- 1], compute k3*Q1 +Q2 = (x1,y1)    
Compute r=x1+e mod n(r!=0)    
Compute S2=d2*k3 mod n   
Compute S3 = d2(r + k2)mod n   
发送r,s2,s3   
# 运行指导
运行在IDEL上
# 截图
![image](https://user-images.githubusercontent.com/105595347/181909095-a45555e5-97b2-4cf6-bc1e-908a40ba6200.png)

# 贡献
个人独立完成

