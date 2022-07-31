# 代码说明
在该过程中， 

公钥为P=[(d1*d2)^(-1) - 1]G  

私钥为d=(d1*d2)^(-1) - 1   

加密过程：

选择k∈[1，N-1]，C1=kG=(x1,y1)

计算kP=(x2,y2)

t=KDF(x2||y2,klen)

C2=M^t

c3=H(x2||M||y2)

通过socket套接字，在进行两个进程之间利用sm2进行加密通话，对于得到的密文进行解密  
具体过程如下：

(1)解密方生成私钥d1∈[1,N-1]，加密方生成私钥d2∈[1,N-1]

(2)解密方得到密文C=C1||C2||C3,检查C1！=0，计算T1=d1^(-1)*C1并发送给加密方

(3)加密方计算出T2=d2^(-1)*T1，将T2发送给解密方

(4)解密明文：

    计算T2-C1=(x2,y2)=[(d1*d2)^(-1) - 1]C1=kP

    计算t=KDF(x2||y2,klen)

    计算m=C2^t

    计算u=hash(x2||m||y2)

    如果u=C3输出m




# 运行指导
运行在IDEL上
# 截图
![image](https://user-images.githubusercontent.com/105595347/181579622-2c12bf1d-7741-4dd1-86dc-9d87bdbbf6e2.png)
![image](https://user-images.githubusercontent.com/105595347/181580669-7567acdc-963d-48d1-93c0-d874354e24c3.png)

# 贡献
个人独立完成
