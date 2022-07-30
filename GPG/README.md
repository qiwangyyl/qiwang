# 代码说明
提前规定好sm2非对称加密的公私钥对，并将公钥传递给对方，对方利用公钥加密对称密钥，利用对称密钥加密消息连同加密后的对称密钥一起发送过来，收到后利用私钥解密得到对称密钥，利用对称密钥可以解密出明文消息。
# 运行指导
在idel上运行，若遇到点恰好不在椭圆曲线上时，则重新运行
# 截图
![image](https://user-images.githubusercontent.com/105595347/181133449-3505645e-694b-4f51-b27e-03eaf78b41d2.png)
含sm2实现：
![image](https://user-images.githubusercontent.com/105595347/181717030-38ae03bd-3915-4ec1-9dcf-16f953a7887e.png)

# 贡献
王淇独立完成
