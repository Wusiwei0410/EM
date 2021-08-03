import numpy as np

def EM( tao_est , p_est , q_est, Obs_seq , batch_size , n ) :
    t = 0
    while (t < 10):
        # 这里简单点的设置了一次终止条件--迭代10次
        # 如果需要通过计算容忍度来更改终止条件可以自己设置
        t = t + 1
        print("开始训练")
        for i in range(batch_size):
            u_B = []
            Y = []
            for j in range(n - 1):
                y = Obs_seq[i, j]  # 将当前的观测结果取出
                Y.append(y)
                # 先是E步，计算隐藏变量的概率
                if y == 1:
                    u_B.append((tao_est * p_est) / (tao_est * p_est + (1 - tao_est) * q_est))
                else:
                    u_B.append((tao_est * (1 - p_est)) / (tao_est * (1 - p_est) + (1 - tao_est) * (1 - q_est)))
            u_B = np.mat(u_B)
            Y = np.mat(Y)
            tao_est = u_B.sum() / (n - 1)
            p_est = (u_B * Y.T)[0, 0] / u_B.sum()
            q_est = ((1 - u_B) * Y.T)[0, 0] / ((1 - u_B).sum())
        print(tao_est, p_est, q_est)

    print("结束")

if __name__ == "__main__" :
    tao_est , p_est , q_est = 0.4 ,0.6 , 0.7 #初始化需要估计的参数

    batch_size = 1
    n = 11
    Obs_seq = np.mat( [ 1 , 1 , 0  , 1 , 0 , 0 , 1 , 0 , 1 , 1 ] )
    EM(tao_est, p_est, q_est, Obs_seq, batch_size, n)

    tao_est, p_est, q_est = 0.5, 0.5, 0.5  # 初始化需要估计的参数
    EM(tao_est, p_est, q_est, Obs_seq, batch_size, n)