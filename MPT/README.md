# 代码思路
MPT树中的节点包括空节点（在代码中是一个空串）、叶子节点（leaf，表示为[key,value]的一个键值对，其中key是key的一种特殊十六进制编码，value是value的RLP编码）、扩展节点（extension，也是[key，value]的一个键值对，但是这里的value是其他节点的hash值，这个hash可以被用来查询数据库中的节点。也就是说通过hash链接到其他节点）和分支节点（branch，因为MPT树中的key被编码成一种特殊的16进制的表示，再加上最后的value，所以分支节点是一个长度为17的字典）

定义leaf类、extension类、branch类表示各种节点类型。

其中leaf类定义包括类型、键值key、value值、前缀、节点的hash值以及节点下数据的hash值，如下所示：
![image](https://user-images.githubusercontent.com/105595347/181915189-719503ae-507c-4169-85f1-108026708432.png)
扩展节点与叶子节点类似，只是把branch节点作为extension节点组成元素，定义extension类如下所示：
![image](https://user-images.githubusercontent.com/105595347/181915590-1af0472f-2c20-408c-b2dd-6b8d7db09bce.png)

分支节点包括类型与长为17的字典，分支节点前16个元素对应着key中的16个可能的十六进制字符，如果有一个[key,value]对在这个分支节点终止，最后一个元素代表一个值，即分支节点既可以搜索路径的终止也可以是路径的中间节点，在该实验的测试代码中并未加入太多节点，如下所示：
![image](https://user-images.githubusercontent.com/105595347/181915664-e1cd96e0-0ca6-49e3-ae0f-897d31e04b61.png)

定义树的类，其中包括初始化函数、创建叶子节点、创建扩展节点、获取前缀不同处索引、添加节点、向前添加扩展节点、向后添加扩展节点、更新树的value和hash值的函数。    

测试是添加一个键为123、值为a的节点，并更新打印出该树。
# 运行指导
在idel上运行
# 截图
![image](https://user-images.githubusercontent.com/105595347/181798657-30d2b423-0364-40ae-b397-e8ca153ad73f.png)
# 贡献
王淇独立完成
