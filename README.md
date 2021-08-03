抛硬币问题

问题描述

有三枚硬币，分别是A,B,C。这些硬币正面出现的概率分别是\pi、p、q。每次试验：先投硬币A，如果出现正面，则选硬币B，反面选硬币A；然后掷选出的硬币，正面记作1，反面记作0；在仿真的时候，我的程序仿真了五组数据作训练数据，然后每组数据在掷完硬币A后，又掷了20次。

参数描述

该问题中的参数\pi、p、q，是我们需要估计的；每次抛硬币的结果是可以观测到的数据变量，而每次掷硬币A的结果是没有提供的，是隐变量。因此，需要用EM算法进行估计。



EM程序介绍

抛硬币问题EM求解_main.py文件是主函数，可以直接运行。该主程序实现了解决抛硬币问题的EM算法，通过随机数产生观测序列和状态序列，并使用EM算法估计随机数。

封装测试李航书里的例子.py文件，将前面main函数里的EM算法部分单独进行封装，输入李航老师书里抛硬币问题里的数据，与李航老师书里计算的结果进行比对。



测试结果

运行李航老师书里的例子，和书上给出的结果一致，证明了程序的正确性。

此外，通过改变给定的\pi、p、q的初值，无论是李航老师书里的数据，还是通过随机数仿真的结果，最后稳定结果都很依赖初值。

