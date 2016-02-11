import sys
import os
import numpy as np
import string
from sklearn import svm,datasets

process_txt = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/nomaltext_process.txt',"r")
# f_w = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/nomaltext_process.txt',"w")
# f_X = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/X.txt',"w")
# f_y = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/y.txt',"w")

list_r = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/key_list.txt','r')

list_r = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/key_list.txt','r')
key_list=[]
all_lines = list_r.readlines()
for each_line in all_lines:
    key_list.append(each_line.strip())
# print len(key_list)

X = np.zeros([567,44],int)
y = np.hstack([np.ones([236],int),np.zeros([331],int)])

print y
n = 0
j = 0