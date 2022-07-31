# 代码说明
实现了在ECDSA签名、sm2签名下由已知的泄露的k退出私钥d的代码

ECDSA签名：d=r^(-1)*(k*s-e)

sm2签名：d=(r+s)^(-1)*(k-s)

# 运行指导
在idel上运行
# 截图
ECDSA签名：

![image](https://user-images.githubusercontent.com/105595347/182008311-08833bfc-3924-4c1a-b92b-e3827bf320ef.png)
sm2签名:

![image](https://user-images.githubusercontent.com/105595347/182008641-13974dea-10c7-4fff-9784-d58ec5e3d115.png)

# 贡献
个人独立完成

