# 代码说明
birthattack:
随机选取2个报文，以这2个报文作为杂凑函数的输入，计算出相应的杂凑值，寻找使H(m1)=H(m2)成立的不同元m1和m2，如果找到，就将(m1,m2)作为结果输出，算法终止;

rhoattack:
随机选取报文作为杂凑函数的输入，计算出相应的杂凑值，加入集合中，按照相应的计算函数计算下一次输入，不停迭代形成输入输出集合，寻找使H(m1)=H(m2)成立的不同元m1和m2，如果找到，就将(m1,m2)作为结果输出，算法终止;
# 运行指导
birthattack运行在idel上

rhoattack运行在visual studio上
# 截图
birthattack:由于运行效率较低，运行出前4位相等的截图如下：
![image](https://user-images.githubusercontent.com/105595347/181131377-041606f0-d9b0-4c80-99ce-538d451fa6fd.png)

rhoattack:由于运行效率较低，运行出前4位相等的截图如下：
![image](https://user-images.githubusercontent.com/105595347/181131586-e17e8c10-265d-4676-8a0f-8d0a77631987.png)


# 贡献
个人独立完成
