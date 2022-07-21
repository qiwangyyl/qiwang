## 十万节点的Merkle-Tree
# 实验思路
1.引入sha256库函数，以及string、random模块，定义信息中的字符范围:字母、数字、标点，将级联前缀0x00以及0x01、采用sha256进行hash都定义成函数，

2.定义一个类MerkleTree，其中的初始化函数包括初始化叶子节点的列表、根节点、记录左右的字典，merkle函数计算出所有节点并将左右标记计算出来，hashnode函数计算出根节点，path函数计算出从m到根节点需要的hash值，以便进行存在性证明，paths函数计算出叶子节点hash值并传入path函数进行计算，proof函数喜欢如节点位置以及信息可计算出根节点信息，雨一直信息相对比，若一致则证明存在。

3.build函数建立具有指定个数的默克树的所有叶子节点


# 实验结果
![image](https://user-images.githubusercontent.com/105595347/180140203-932a20d7-3e8f-479a-bee1-ac195179688c.png)
