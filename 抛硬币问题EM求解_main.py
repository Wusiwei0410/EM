import numpy as np

if __name__ == "__main__" :
    tao , p , q = 0.5 , 0.4 , 0.6  #三种硬币投掷出证明的概率——参数初始化

    #进行仿真，先抛一次硬币A，然后接着抛20次硬币
    #仿真出5组数据，即5个batch
    tao_est , p_est , q_est = 0.2 ,0.2 , 0.2 #初始化需要估计的参数
    batch_size = 5
    n = 21 #先投一次硬币，然后后面投20次
    rand_rate = np.random.rand( batch_size , n )
    Obs_seq = np.zeros( [ batch_size , n - 1 ] )
    record_B_or_C = [] #记录这次投掷的是B还是C
    for i in range( batch_size ) :
        if rand_rate[ i , 0 ] > tao :
            #投掷20次硬币C
            Obs_seq[ i ][ rand_rate[ i , 1 : n ]  < q ] = 1
            record_B_or_C.append( 2 )
        else :
            #投掷硬币B
            Obs_seq[i][rand_rate[i, 1: n] < p ] = 1
            record_B_or_C.append(1)

    t = 0
    while( t < 10 ) :
        t = t + 1
        print( "开始训练" )
        for i in range( batch_size ) :
            u_B = []
            Y = []
            for j in range( n - 1 ) :
                y = Obs_seq[ i , j ] #将当前的观测结果取出
                Y.append( y )
                #先是E步，计算隐藏变量的概率
                if y == 1 :
                    u_B.append(( tao_est * p_est ) / ( tao_est * p_est + ( 1 - tao_est ) * q_est ))
                else :
                    u_B.append((tao_est * ( 1 - p_est )) / (tao_est * ( 1 - p_est ) + (1 - tao_est) * ( 1 - q_est) ))
            u_B = np.mat( u_B )
            Y = np.mat( Y )
            tao_est = u_B.sum() / ( n - 1 )
            p_est = (u_B * Y.T)[ 0 , 0 ] / u_B.sum()
            q_est = (( 1 - u_B ) * Y.T)[ 0 , 0 ] / ( ( 1 - u_B ).sum() )
        print( tao_est , p_est , q_est )

    # print( Obs_seq )
    # print( record_B_or_C )


    print( "结束" )