# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 10:03:31 2017

@author: Administrator
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt


#img = cv2.imread('1.jpg',1)
def build_filters():
    angles=[0,30,60,90,120,150]#角度
    longs=[3,8,13,18,23,28]#波长
    ksize=21
    sig=5
    gm=1
    ps=0
    filters=[]
    for long in longs:
        for angle in angles:
            th=angle*np.pi/180
            lm=long
            kern = cv2.getGaborKernel((ksize, ksize),sig,th,lm,gm,ps)
            #ksize 滤波核尺寸，sig带宽，th倾斜角度  ，lm 波长 ，gm=1空间纵横比 
            #ps 相位，一般为0
            kern /= 1.5*kern.sum()#?
            filters.append(kern)
            #print(len(filters))
    return filters

names=build_filters()
img = cv2.imread('8.jpg',0)
img1 = np.float32(img)
fimgs=[]
for name in names:
    result = cv2.filter2D(img1, -1, name)
    fimgs.append(result)
print(fimgs)


fig = plt.gcf()
fig.set_size_inches(9, 5)#输出图表的整体尺寸
plt.figure(1)#创建图表1
for i in range(6):
    plt.subplot(6,12,i*12+1),plt.imshow(fimgs[i*6+0],cmap='gray')
    plt.xticks([]),plt.yticks([])#去掉刻度
    plt.ylabel(i*5+3, fontsize=10,)#x轴标题，大小
    plt.subplot(6,12,i*12+2),plt.imshow(names[i*6+0],cmap='gray')
    plt.xticks([]),plt.yticks([])
    if i==5:
        plt.xlabel(0, fontsize=10)
        
    plt.subplot(6,12,i*12+3),plt.imshow(fimgs[i*6+1],cmap='gray')
    plt.xticks([]),plt.yticks([])
    plt.subplot(6,12,i*12+4),plt.imshow(names[i*6+1],cmap='gray')
    plt.xticks([]),plt.yticks([])
    if i==5:
        plt.xlabel(30, fontsize=10)
        
    plt.subplot(6,12,i*12+5),plt.imshow(fimgs[i*6+2],cmap='gray')
    plt.xticks([]),plt.yticks([])
    plt.subplot(6,12,i*12+6),plt.imshow(names[i*6+2],cmap='gray')
    plt.xticks([]),plt.yticks([])
    if i==5:
        plt.xlabel(60, fontsize=10)
        
    plt.subplot(6,12,i*12+7),plt.imshow(fimgs[i*6+3],cmap='gray')
    plt.xticks([]),plt.yticks([])
    plt.subplot(6,12,i*12+8),plt.imshow(names[i*6+3],cmap='gray')
    plt.xticks([]),plt.yticks([])
    if i==5:
        plt.xlabel(90, fontsize=10)
        
    plt.subplot(6,12,i*12+9),plt.imshow(fimgs[i*6+4],cmap='gray')
    plt.xticks([]),plt.yticks([])
    plt.subplot(6,12,i*12+10),plt.imshow(names[i*6+4],cmap='gray')
    plt.xticks([]),plt.yticks([])
    if i==5:
        plt.xlabel(120, fontsize=10)
        
    plt.subplot(6,12,i*12+11),plt.imshow(fimgs[i*6+5],cmap='gray')
    plt.xticks([]),plt.yticks([])
    plt.subplot(6,12,i*12+12),plt.imshow(names[i*6+5],cmap='gray')
    plt.xticks([]),plt.yticks([])
    if i==5:
        plt.xlabel(150, fontsize=10)#x轴标题，大小
plt.show()


"""   
def process(filters):
    for p in range(36):
        print(filters[p])
 
n=process(m) 
print(n)  

def getGabor(img,filters):
    res = [] #滤波结果
    for i in range(len(filters)):        
        res1 = process(img, filters[i])
        res.append(np.asarray(res1))
    pl.figure(2)
    for temp in range(len(res)):
        pl.subplot(6,6,temp+1)
        pl.imshow(res[temp], cmap='gray' )
    pl.show()
    return res  #返回滤波结果,结果为24幅图，按照gabor角度排列"""
"""          
            lm=long
            th=v*np.pi/180
            kern = cv2.getGaborKernel((ksize, ksize),sig,th,lm,gm,ps)
            #ksize 滤波核尺寸，sig带宽，th倾斜角度  ，lm 波长 ，gm=1空间纵横比 ，ps 相位，一般为0
            kern /= 1.5*kern.sum()
            filters.append(kern)
            return filters
n=build_filters()
def process(img, filters):
    accum = np.zeros_like(img)
    for kern in filters:
        fimg = cv2.filter2D(img, cv2.CV_8UC3, kern)
        np.maximum(accum, fimg, accum)
    return accum
m=process('1.jpg',n)
print(m)"""