# 代码说明
ECMH思想为将哈希映射成椭圆曲线上的点，然后利用ECC的加法添加信息，将信息存储在元组中，对元祖中的每一个元素调用函数得到对应的哈希映射成椭圆曲线上的点；
其中相同点的加法定义为函数elliptic_double，不同点的加法定义为elliptic_add。其中参数按照标准进行赋值。
# 运行指导
在idel中运行
# 截图
![image](https://user-images.githubusercontent.com/105595347/181192980-44b58670-6d3f-4f40-bf7c-a06ef17d7cd1.png)
# 贡献
王淇独立完成
