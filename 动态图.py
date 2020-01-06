# -*- coding: UTF-8 -*-
'''
@Author ：wangjie
@Date   ：2020/1/6 9:41
@Desc   ：
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation   #导入负责绘制动画的接口
#其中需要输入一个更新数据的函数来为fig提供新的绘图信息

fig, ax = plt.subplots()
x, y= [], []
line, = plt.plot([], [], '.-',color='orange')
nums = 50   #需要的帧数

def init():
    ax.set_xlim(-5, 60)
    ax.set_ylim(-3, 3)
    return line

def update(step):
    if len(x)>=nums:       #通过控制帧数来避免不断的绘图
        return line
    x.append(step)
    y.append(np.cos(step/3)+np.sin(step**2))    #计算y
    line.set_data(x, y)
    return line

ani = FuncAnimation(fig, update, frames=nums,     #nums输入到frames后会使用range(nums)得到一系列step输入到update中去
                    init_func=init,interval=20)
plt.show()