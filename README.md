一.

小组成员王淇，账户名称为wqlly,个人独立完成。  
二.

项目简介	| 项目名称	| 完成人
----------------------------------------------------------------|--------------------------------------------------------------------------------------|-------------
 随机选取两个消息，实现生日碰撞攻击    | implement the naïve birthday attack of reduced SM3 |	王淇
选取一个数通过迭代计算并hash，找到hash值相等的两个消息|   implement the Rho method of reduced SM3	|王淇
利用多线程实现sm3的优化| do your best to optimize SM3 implementation (software)	|王淇
通过添加一个附加消息来伪造消息可以计算出相应hash值| implement length extension attack for SM3	|王淇
生成十万节点的Merkle-Tree	| Impl Merkle Tree following RFC6962  |	王淇
利用多线程、simd指令、循环展开优化 |	实现及优化SM4	| 王淇
在椭圆曲线数字签名算法（ECDSA）下反推公钥	| report on the application of this deduce technique in Ethereum with ECDSA  |	王淇
实现sm2时通过确定性的算法生成保密且唯一的k	| impl sm2 with RFC6979   |	王淇
利用椭圆曲线上点的加减表示信息的增删|Implement the above ECMH scheme  |	王淇
通过公钥加密私钥、私钥加密信息的方式传递消息|Implement a PGP scheme with SM2 | 	王淇
socket编程实现真实网络上sm2签名|implement sm2 2P sign with real network communication |	王淇
socket编程实现真实网络上sm2解密|implement sm2 2P decrypt with real network communication  |	王淇
伪造e与签名通过验证| forge a signature to pretend that you are Satoshi  | 	王淇
融合了默克尔树和前缀树两种树结构，存储任意长度的key-value键值对数据|research report on MPT  |	王淇
实现ECDSA的已知k推出d|verify the above pitfalls with proof-of-concept code  |王淇


三.

完成项目|
------------------------------------|
implement the naïve birthday attack of reduced SM3   |
implement the Rho method of reduced SM3   |
implement length extension attack for SM3  | 
do your best to optimize SM3 implementation (software)|      
Impl Merkle Tree following RFC6962    |
实现及优化SM4   |
report on the application of this deduce technique in Ethereum with ECDSA   |
impl sm2 with RFC6979   |
Implement the above ECMH scheme   |
Implement a PGP scheme with SM2   |
implement sm2 2P sign with real network communication   |
implement sm2 2P decrypt with real network communication | 
forge a signature to pretend that you are Satoshi   |
research report on MPT  |
verify the above pitfalls with proof-of-concept code  |

未完成项目|
------------------------------------|    
Try to Implement this scheme(below) |
PoC impl of the scheme, or do implement analysis by Google  |
send a tx on Bitcoin testnet, and parse the tx data down to every bit, better write script yourself   |
Find a key with hash value “sdu_cst_20220610” under a message composed of your name followed by your student ID. For example, “San Zhan 202000460001”.  |
Find a 64-byte message under some k fulfilling that their hash value is symmetrical.  |
![image](https://user-images.githubusercontent.com/105595347/181213346-c85d0b42-a9b5-4c7f-835d-0fc893561f2d.png) |

有问题的项目：verify the above pitfalls with proof-of-concept code只实现了一部分
