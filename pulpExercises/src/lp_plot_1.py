# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 09:46:32 2018
@author: siriJR

Abstract:
通过图解法求解简单线性规划
"""


"""
question：null

objective： Z = 4x + 3y

constraints:
x ≥ 0
y ≥ 2
2y ≤ 25 - x
4y ≥ 2x - 8
y ≤ 2x - 5
"""


import numpy as np
import matplotlib.pyplot as plt


#产生0-20之间的随机数2000个
x=np.linspace(0,20,2000)

y1=x*0+2
y2=(25-x)/2.0
y3=(2*x-8)/4.0
y4=2*x-5


# Make plot
plt.plot(x, y1, label=r'$y\geq2$')
plt.plot(x, y2, label=r'$2y\leq25-x$')
plt.plot(x, y3, label=r'$4y\geq 2x - 8$')
plt.plot(x, y4, label=r'$y\leq 2x-5$')
plt.xlim((0, 16))
plt.ylim((0, 11))
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')

# 填充
y5 = np.minimum(y2, y4) #取两条直线下方的区域
y6 = np.maximum(y1, y3) #取两条直线上方的区域
plt.fill_between(x, y5, y6, where=y5>y6, color='grey', alpha=0.5)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


#可知最优解是四个角中的一个，分别带入目标函数，取最大既最优解
#x = 14.5
#y = 5.25
#Z = 73.75


"""
以下通过pulp库求解
"""

import pulp

model = pulp.LpProblem("My LP Problem", pulp.LpMaximize)


x = pulp.LpVariable('x', lowBound=0, cat='Continuous') #可以是Continuous和Integer
y = pulp.LpVariable('y', lowBound=2, cat='Continuous')

#目标
model+=4*x+3*y,'z'

#约束
model+= 2*y <= 25 - x
model+= 4*y >= 2*x - 8
model+=y <= 2*x - 5

#求解
model.solve()

for variable in model.variables():
    print ("{} = {}".format(variable.name, variable.varValue))

print (pulp.value(model.objective))

"""
结果
x = 14.5
y = 5.25
73.75
"""

tmp=1

