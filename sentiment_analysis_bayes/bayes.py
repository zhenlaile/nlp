# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 13:40:26 2018

@author: cm
"""
import os
import jieba
import numpy as np


pwd = os.path.dirname(os.path.abspath(__file__))

# 朴素贝叶斯分类函数
def classify(vec2Classify,p0Vec,p1Vec,pClass1):
    p1=sum(vec2Classify*p1Vec) + np.log(pClass1)
    p0=sum(vec2Classify*p0Vec) + np.log(1-pClass1)
    if p1>p0:
        return 1
    else:
        return 0

#加载模型
def load_p0Vec_p1Vec_pClass1():
    f = os.path.join(pwd,'parametre_pearson_40000','p0Vec.txt')
    fp=open(f,encoding='utf-8');lines=fp.readlines();fp.close()
    p0Vec=[]
    for i  in lines: 
        p0Vec.append(float(i))
    p0Vec = np.array(p0Vec)
    #
    f = os.path.join(pwd,'parametre_pearson_40000','p1Vec.txt')
    fp=open(f,encoding='utf-8');lines=fp.readlines();fp.close()
    p1Vec=[]
    for i  in lines: 
        p1Vec.append(float(i))
    p1Vec = np.array(p1Vec)
    #
    f = os.path.join(pwd,'parametre_pearson_40000','pClass1.txt')
    fp=open(f,encoding='utf-8'); lines=fp.readlines();fp.close()
    pClass1 = float(lines[0])
    return p0Vec,p1Vec,pClass1



# 读取停用词(或者标点符号)
f = os.path.join(pwd,'dict','ponctuation_sentiment.txt')
fp = open(f,encoding='utf-8')
lines = fp.readlines()
fp.close()
stopwords=[line.strip('\n')  for line in lines]
  
  
# 去除停用词 ok
def drop_stopwords(sentence):
    segResult = jieba.lcut(sentence)


    newSent = []
    for word in segResult:
        if word in stopwords:
            continue
        else:
            newSent.append(word)
    return newSent


#读取词汇特征
f = os.path.join(pwd,'data','vocabulary_pearson_40000.txt')
fp = open(f,encoding='utf8')
vocabulary = fp.readlines()
fp.close()
vocabulary = [texte.replace('\n','') for texte in vocabulary ]
def set_vector(sentence):
    line = drop_stopwords(sentence)
    vector = []
    for word in vocabulary:
        vector.append(int(line.count(word)))
    return vector


#利用模型预测
p0Vec,p1Vec,pClass1 = load_p0Vec_p1Vec_pClass1()
def predictionBayes(Sentence):
    vector  = set_vector(Sentence)#
    p = classify(vector,p0Vec,p1Vec,pClass1)
    return p


if __name__ =='__main__':
    print(predictionBayes('我爱武汉'))
    
    
    
    
    