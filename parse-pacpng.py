import re
import dpkt
import sys
import os
import urllib
import numpy as np
import string
from sklearn import svm,datasets


#======================================process data======================================================

f = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/5.pcap',"r")
f_w = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/nomaltext_process.txt',"w")
# f_X = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/X.txt',"w")
# f_y = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/y.txt',"w")

list_r = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/key_list.txt','r')
key_list=[]
all_lines = list_r.readlines()
for each_line in all_lines:
    key_list.append(each_line.strip())
# print len(key_list)

pcap = dpkt.pcap.Reader(f)

X = np.zeros([236,44],int)
y = np.ones([236],int)

n = 0
j = 0

# print X(0,0)

for ts, buf in pcap:
    # print ts,len(buf)
    eth = dpkt.ethernet.Ethernet(buf)
    ip = eth.data
    tcp = ip.data

    # print tcp.sport
    # print tcp.dport
    try:
        if tcp.dport == 80 and len(tcp.data) > 0:
            http = dpkt.http.Request(tcp.data)
            # print http.method
            uri = http.uri
            uri = uri.lower()
            uri = re.sub(r'[0-9]+', ' number ', uri)  
            uri = re.sub(r'%', ' ',uri)
            uri = re.sub(r'\-', ' ',uri)
            txt_array = string.split(uri,' ')
            # raw_input("pause")
            for i in range(0, len(txt_array)):
                # print txt_array[i]
                # print 
                for j in range(0,len(key_list)):
                    # print txt_array[i]
                    # print len(key_list)
                    # print X[n,j]
                    if txt_array[i] == key_list[j]:
                        X[n,j] = 1

            # raw_input('pause:')
            f_w.write('%s%s' % (urllib.unquote(uri),os.linesep))
            n = n+1
            # print http.version
            # print http.headers
    except:
        pass

    # raw_input()


f.close()
f_w.close()
list_r.close()


#================================Support Vector Machine================================

# print X
# print y



h = 0.02

C = 1.0
svc = svm.SVC(kernel='linear',C=C).fit(X,y)
rbf_svc = svm.SVC(kernel='rbf',gamma=0.7,C=C).fit(X,y)
poly_svc = svm.SVC(kernel='poly',degree=3,C=C).fit(X,y)
lin_svc = svm.LinearSVC(C=C).fit(X,y)



#==============================Predict=========================================
predict_f = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/4.pcap',"r")
predict_pcap = dpkt.pcap.Reader(predict_f)

X_pre = np.zeros[1,44]

for ts, buf in predict_pcap:
    # print ts,len(buf)
    eth = dpkt.ethernet.Ethernet(buf)
    ip = eth.data
    tcp = ip.data

    # print tcp.sport
    # print tcp.dport
    try:
        if tcp.dport == 80 and len(tcp.data) > 0:
            http = dpkt.http.Request(tcp.data)
            # print http.method
            uri = http.uri
            uri = uri.lower()
            uri = re.sub(r'[0-9]+', ' number ', uri)  
            uri = re.sub(r'%', ' ',uri)
            uri = re.sub(r'\-', ' ',uri)
            txt_array = string.split(uri,' ')
            # raw_input("pause")
            for i in range(0, len(txt_array)):
                # print txt_array[i]
                # print 
                for j in range(0,len(key_list)):
                    # print txt_array[i]
                    # print len(key_list)
                    # print X[n,j]
                    if txt_array[i] == key_list[j]:
                        X_pre[0,j] = 1

            # raw_input('pause:')
            f_w.write('%s%s' % (urllib.unquote(uri),os.linesep))
            n = n+1
            # print http.version
            # print http.headers
    except:
        pass

print svc.predict(X)