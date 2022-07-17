## sm2_with_RFC6979实验原理
wangqi
# 实验思路
1.按照sm2标准规定系统曲线参数A、B，以及基点G的横纵坐标，规定有限域的阶以及椭圆曲线的阶；

2.生成公私钥对，私钥为随机生成的大整数，公钥为椭圆曲线上的点，生成公钥P_A即私钥乘规定的基点；

3.定义传递的消息以及签名者用户A具有长度为ENTLA比特的可辨别标识ID；

4.预计算生成Z_A，其中Z_A=H256(ENTLA||ID||a||b||G_X||G_Y||pub_x||pub_y)；

5.进行签名：利用私钥、信息以及预计算生成的Z_A，计算（r,s），e=SM3(Z_A||m),随机生成k，使(x_1,y_1)=[k]G,利用生成的e与x_1计算r,其中r=(e+x_1)mod n，然后计算s=((1+private_key)^(-1)⋅(k−r⋅private_key))mod n；

6.进行验证：利用公钥、ID、信息以及签名（r,s）,首先通过预计算生成Z_A，计算m*=Z_A||m，e=SM3(m*),t=(r+s)%N，使(x_1,y_1)=[s]G+[t]P_A,利用生成的e与x_1计算R,其中R=(e+x_1)mod n，然后利用得到的签名r与R进行比较，如果相等那么验证成功。
# 实验结果
![image](https://user-images.githubusercontent.com/105595347/179397046-57592b45-608b-45ff-83ef-5be2fb1a45f2.png)
