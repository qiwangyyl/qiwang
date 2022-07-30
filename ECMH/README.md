# 代码说明
ECMH思想为将哈希映射成椭圆曲线上的点，然后利用ECC的加法添加信息，将信息存储在元组中，对元组中的每一个元素调用函数得到对应的哈希映射成椭圆曲线上的点。    

相同点的加法定义为函数elliptic_double，不同点的加法定义为elliptic_add，椭圆曲线上的乘法运算定义为elliptic_multiply。 定义函数QR以便于进行二次剩余计算。  

定义H函数传入元组，对元组中的数据遍历并通过hash后得到x，计算出对应的y值，得到椭圆曲线上的点，将元素对应的椭圆曲线上的点相加得到结果。    

其中参数按照标准进行赋值，如下所示：
![image](https://user-images.githubusercontent.com/105595347/181914147-124c9ce5-8682-435c-b40f-62f426f51141.png)

# 运行指导
在idel中运行
# 截图
![image](https://user-images.githubusercontent.com/105595347/181192980-44b58670-6d3f-4f40-bf7c-a06ef17d7cd1.png)
# 贡献
王淇独立完成
