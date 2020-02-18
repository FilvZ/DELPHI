#!/usr/bin/env python
# encoding: utf-8
'''
@author: zenglei
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: 497230472@qq.com
@software: garner
@file: cs.py
@time: 2018-02-08 18:22
@desc:
'''
import random
import timeit
game=[[2, 4, 4, 2],
      [4, 2, 4, 2],
      [2, 0, 2, 2],
      [4, 2, 2, 2]]
# game=[[0, 0, 0, 0],
#       [0, 0, 0, 0],
#       [0, 0, 0, 0],
#       [0, 0, 0, 0]]
# 所有状态值初始默认为-1  运行赋值 0 / 1
G_key=-1  #键值是否有效
G_move=-1 #移动是否有效
G_add=-1  #数值是否累加
G_new=-1  #是否新增数值
G_over=-1 #游戏是否结束

def p(v):
    print('{0:4} {1:4} {2:4} {3:4}'.format(v[0][0], v[0][1], v[0][2], v[0][3]))
    print('{0:4} {1:4} {2:4} {3:4}'.format(v[1][0], v[1][1], v[1][2], v[1][3]))
    print('{0:4} {1:4} {2:4} {3:4}'.format(v[2][0], v[2][1], v[2][2], v[2][3]))
    print('{0:4} {1:4} {2:4} {3:4}'.format(v[3][0], v[3][1], v[3][2], v[3][3]))

def x(v):
    for j in range(len(v)):
        for i in range(v[j].count(0)):
            v[j].remove(0)

def replse(v):
    sm=-1
    for j in range(len(v)):
        for i in range(len(v[j])):
            if j <= i:
                sm=v[i][j]
                v[i][j]=v[j][i]
                v[j][i]=sm

def replace(v):
    vl = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]
    for j in range(len(v)):
        for i in range(len(v[j])):
            vl[j][i] = v[i][j]
    return vl

def left(v):
    x(v)
    for j in range(len(v)):
        zeros = [0 for x in range(4 - len(v[j]))]
        v[j].extend(zeros)
    for j in range(len(v)):
        for i in range(len(v[j])):
            if i + 1 != len(v[j]) and v[j][i] == v[j][i + 1]:
                v[j][i] *= 2
                v[j][i+1] = 0
        zeros = [0 for x in range(4 - len(v[j]))]
        v[j].extend(zeros)
    x(v)
    for j in range(len(v)):
        zeros = [0 for x in range(4 - len(v[j]))]
        v[j].extend(zeros)

def add(v):
    mdict=dict()
    # 计数器
    num=0
    # 获取随机值
    c = random.choice([2, 2, 2, 4])

    for j in range(len(v)):
        for i in range(len(v[j])):
            if v[j][i]==0:
                #将值为0的位置信息保存到mdict
                mdict[num] = (j, i)
                # 计数器累加
                num+=1

    num = indx_(num)

    # 可添加数值
    if num !=-1:
        print(num)
        x=mdict[num][0]
        y=mdict[num][1]
        print(mdict[num][0])
        print(mdict[num][1])
        v[x][y]=c
    else: G_new=1

def indx_(num = 0):
    # 可以添加基础数值
    if num !=0:
        # 随机可添加数值位置
        num = random.randint(0, num - 1)
        return num
    else:
        return -1

def run1(v):
    replse(v)
    left(v)
    replse(v)

def run2(v):
    v = replace(v)
    left(v)
    v = replace(v)
# run(game)

# t1= timeit.timeit('run(game)',setup=game, number=100)

# print(str(timeit.timeit('run1(game)',setup='from __main__ import run1, game', number=10000))) #0.027510935317282225 2.4428230659342747
# print(str(timeit.timeit('run2(game)',setup='from __main__ import run2, game', number=10000))) #0.024077451122924344 2.4225615190609533
print(str(timeit.repeat('run1(game)',setup='from __main__ import run1, game', repeat=10, number=10000))) #0.027510935317282225 2.4428230659342747
p(game)
print('')
print(str(timeit.repeat('run2(game)',setup='from __main__ import run2, game', repeat=10, number=10000))) #0.024077451122924344 2.4225615190609533
p(game)
