## 在椭圆曲线数字签名算法（ECDSA）下反推公钥
# 实验思路
定义参数如下所示：
![image](https://user-images.githubusercontent.com/105595347/181917835-5d33f72a-3e2e-43ef-8b5d-41b0cb363b42.png)

1、首先实现该数字签名算法，公钥为d[G]，随机选k，计算R=kG，则r为R横坐标，计算e=hash(mes)，s=k^(-1)*(e+dr)mod n,生成签名（r,s）;

2、反推密钥时，计算出x=r%P，y^2=x^3+Ax+B，利用计算二次剩余的函数计算y^2在mod p下的平方根，计算出关于x周对称的两个点，得到相应点的横纵坐标，计算e=hash(mes)，s*k[G]=(e+dr)[G]mod n,可以计算出d*r[G],利用库函数中求逆 的函数可以求出r的逆并得到公钥;

3、得到的公钥可验证有真实的公钥。
# 运行指导
在idel上运行

# 实验结果
![image](https://user-images.githubusercontent.com/105595347/179545828-dbd3859e-3d59-4ed9-9113-3daeb4075aa5.png)

# 贡献
个人独立完成
