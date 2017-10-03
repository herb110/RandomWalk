import matplotlib.pyplot as plt

from random_walk import RandomWalk

#只要程序处于活动状态就不断模拟随机漫步
while True:
    #创建一个RandomWalk实例
    rw = RandomWalk(50000)
    rw.fill_walk()
    
    #设置绘图窗口的尺寸
    plt.figure(dpi=128,figsize=(10,6))
    
    #将其中的点绘制出来
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,
            edgecolor= 'none',s=1)
            
    #突出起点和终点
    plt.scatter(0,0,c='orange',edgecolor='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolor='none',
            s=100)
          
    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    
    plt.savefig('random_walk.png',bbox_inches='tight')
    
    keep_running = input("Make another walk? (y/n)")
    if keep_running == 'n':
        break