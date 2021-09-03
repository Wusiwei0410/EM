# 抛硬币问题

## 问题描述

有三枚硬币，分别是A,B,C。这些硬币正面出现的概率分别是$\pi、p、q$。每次试验：先投硬币A，如果出现正面，则选硬币B，反面选硬币A；然后掷选出的硬币，正面记作1，反面记作0；在仿真的时候，我的程序仿真了五组数据作训练数据，然后每组数据在掷完硬币A后，又掷了20次。

##  参数描述

该问题中的参数$\pi、p、q$，是我们需要估计的；每次抛硬币的结果是可以观测到的数据变量，而每次掷硬币A的结果是没有提供的，是隐变量。因此，需要用**EM**算法进行估计。

# EM程序介绍

***抛硬币问题EM求解_main.py***文件是主函数，可以直接运行。该主程序实现了**解决抛硬币问题**的EM算法，通过随机数产生观测序列和状态序列，并使用**EM算法**估计随机数。

***封装测试李航书里的例子.py***文件，将前面**main**函数里的EM算法部分单独进行封装，输入李航老师书里抛硬币问题里的数据，与李航老师书里计算的结果进行比对。

***程序介绍：***在*main*函数里$tao-est,p-est,q-est$​是每次迭代估计的$\pi、p、q$​；$batch-size$​就是产生的序列个数；$n$​​的值是每次仿真实验，包括第一次投掷硬币A和后面投掷硬币B或C的总次数。

***迭代终止条件：***在李航老师的书里，以前后两次迭代参数$\theta$​​​​​或者似然函数期望$Q$​差值的范数小于设置的阈值$\varepsilon$​​​​，则停止迭代；​​我的程序，因为给的数据比较简单，就以迭代10次为终止条件（基本可以达到稳定）；当然这个终止方法可以自己进行更改

# 测试结果

运行李航老师书里的例子，和书上给出的结果一致，证明了程序的正确性。

此外，通过改变给定的$\pi、p、q$的初值，无论是李航老师书里的数据，还是通过随机数仿真的结果，最后稳定结果都很依赖初值。

|你好|
| --- |
| 再见 |

|  你好 |dataset | learning rate | activation function|hidden size|acc | 
|      :----:  | :----: |        :----:  |        :----:     |   :----:  | :----:    |
|   logistic   |   exam |      0.1       |         \         |      \    | 75%       |
|   softmax    |   exam |       0.01     |         \         |      \    | 75%       |
|ANN from Scratch| exam |       0.01    |      sigmoid      |      50    | 75%       |
|ANN from Scratch| exam |       0.005    |      sigmoid      |     100   | 75%       |
|ANN from Scratch| exam |       0.1      |      sigmoid      |     100   | 69%       |
|ANN from Scratch| exam |       0.005     |      sigmoid     |     200   | 71%       |
|ANN from Scratch| exam |       0.005     |      sigmoid     |     500   | 68%       |
|ANN from Scratch| exam |       0.001     |      relu        |     100   | 69%       |
|   softmax    |   iris |       0.1       |         \         |      \    | 93%       |
|ANN from Scratch| iris |       0.1      |      sigmoid      |      50    | 93%       |
|ANN from Scratch| iris |       0.1     |      sigmoid      |     100   | 93%       |
|ANN from Scratch| iris |       0.1      |      sigmoid      |     500   | 93%       |
|ANN from Scratch| iris |       0.01     |      sigmoid     |     100   | 93%       |
|ANN from Scratch| iris |       0.01     |      relu        |     100   | 89%       |
|ANN from Scratch| iris |       0.1     |      relu        |     100   | 90%       |
