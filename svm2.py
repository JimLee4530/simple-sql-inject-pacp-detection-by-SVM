import re
import dpkt
import sys
import os
import numpy as np
import string
import socket
import datetime
from sklearn import svm,datasets


#================================ get (X,y) ==============================


process_txt = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/trainSetProcess.txt',"r")
# f_w = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/nomaltext_process.txt',"w")
# f_X = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/X.txt',"w")
# f_y = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/y.txt',"w")

list_r = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/key_list.txt','r')
key_list=[]
all_lines = list_r.readlines()

m = 1982

for each_line in all_lines:
    key_list.append(each_line.strip())
    # m += 1
# print len(key_list)
# print m
# raw_input('pause')
X = np.zeros([m,len(key_list)],int)
y = np.hstack([np.ones([398],int),np.zeros([1584],int)])

n = 0
all_lines = process_txt.readlines()
for each_line in all_lines:
    txt_array = string.split(each_line,' ')
    # print txt_array
    # print len(txt_array)
    # raw_input('pause')
    for i in range(0, len(txt_array)):
        # print len(key_list)
        for j in range(0,len(key_list)):
            # print "j =", j
            # print "n =", n
            if txt_array[i] == key_list[j]:
                X[n,j] += 1
    n = n + 1



#================================Support Vector Machine================================


h = 0.02

C = 1.0
# svc = svm.SVC(kernel='linear',C=C).fit(X,y)
# rbf_svc = svm.SVC(kernel='rbf',gamma=0.7,C=C).fit(X,y)
# poly_svc = svm.SVC(kernel='poly',degree=3,C=C).fit(X,y)
lin_svc = svm.LinearSVC(C=C, penalty='l1').fit(X,y)


#==============================Predict=========================================
predict_f = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/testSetProcess.txt',"r")

result_f = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/result.txt',"w")

X_pre = np.zeros([1,len(key_list)],int)

y_test = np.hstack([np.ones([1,223], int), np.zeros([1,1336], int)])
y_per = []

n = 0
err = 0
err2 = 0

all_lines = predict_f.readlines()
for each_line in all_lines:
    txt_array = string.split(each_line,' ')
    for i in range(0, len(txt_array)):
        # print len(key_list)
        for j in range(0,len(key_list)):
            # print "j =", j
            # print "n =", n
            if txt_array[i] == key_list[j]:
                X_pre[0,j] += 1
    result = lin_svc.predict(X_pre)
    if result != y_test[0][n]:
        err += 1
        if y_test[0][n] == 0:
            err2 += 1
    n += 1
    print err
    # if result == 1:
        # result_f.write('%s\nIP:%s-->%s   (len=%d ttl=%d) \n dangerous data : %s %s' % (str(datetime.datetime.utcfromtimestamp(ts)),socket.inet_ntoa(ip.src),socket.inet_ntoa(ip.dst),ip.len, ip.ttl, uri_origin,os.linesep))

# for ts, buf in predict_pcap:
#     # print ts,len(buf)
#     eth = dpkt.ethernet.Ethernet(buf)
#     ip = eth.data
#     tcp = ip.data
    
#     # print tcp.sport
#     # print tcp.dport

# #===============================bebug part===================================
#     try:
#         if tcp.dport == 80 and len(tcp.data) > 0:
#             http = dpkt.http.Request(tcp.data)
#             # print http.method
#             uri_origin = http.uri
#             uri = uri_origin.lower()
#             uri = re.sub(r'(http|https)://[^\s]*', ' httpaddr ', uri)
#             uri = re.sub(r'\?', ' question_mask ', uri)
#             uri = re.sub(r'\/',' backslash ', uri)
#             uri = re.sub(r'\%', ' per_cent ', uri)
#             uri = re.sub(r'\-', ' hyphen ', uri)
#             uri = re.sub(r'\'', ' colon ', uri)
#             uri = re.sub(r'\=', ' equality_sign ', uri)
#             uri = re.sub(r'\(', ' left_bracket ', uri)
#             uri = re.sub(r'\)', ' right_bracket ', uri)
#             uri = re.sub(r'\&',' and_mask ',uri)
#             uri = re.sub(r'[0-9]+', ' number ', uri)
#             uri = re.sub(r'\~', ' wave_number ', uri)
#             uri = re.sub(r'\*', ' multiplication_sign ', uri)
#             uri = re.sub(r'\#', ' note_sign ', uri)
#             uri = re.sub(r'\<', ' left_angle_bracket ', uri)
#             uri = re.sub(r'\>', ' right_angle_bracket ', uri)
#             uri = re.sub(r'\@', ' at_sign ', uri)
#             uri = re.sub(r'\+', ' add_sign ', uri)
#             uri = re.sub(r'\;', ' semicolon ', uri)
#             uri = re.sub(r'\{', ' left_curly_braces ', uri)
#             uri = re.sub(r'\}', ' right_curly_braces ', uri)
#             uri = re.sub(r'\!', ' exclamation_mark ', uri)
#             uri = re.sub(r'\|', ' bit_or ', uri)
#             txt_array = string.split(uri,' ')
#             # print txt_array
#             # raw_input('pause')
#             for i in range(0, len(txt_array)):
#                 for j in range(0,len(key_list)):
#                     if txt_array[i] == key_list[j]:
#                         X_pre[0,j] = 1
#             # print X_pre
#             # raw_input('pause')
#             result = lin_svc.predict(X_pre)
#             # result = poly_svc.predict(X_pre)
#             # result = svc.predict(X_pre)
#             # result = rbf_svc.predict(X_pre) #rbf is work!
#             # print result
#             # print y_test[0][n]
#             # raw_input('pause')
#             print result != y_test[0][n]
#             if result != y_test[0][n]:
#                 # print err
#                 # raw_input('pause')
#                 err += 1
#             n += 1
#             print err
#             if result == 1:
#                 # print X_pre
#                 # print 'IP:%s-->%s' % (socket.inet_ntoa(ip.src),socket.inet_ntoa(ip.dst))
#                 # print urllib.unquote(http.uri)
#                 # print str(datetime.datetime.utcfromtimestamp(ts))
#                 result_f.write('%s\nIP:%s-->%s   (len=%d ttl=%d) \n dangerous data : %s %s' % (str(datetime.datetime.utcfromtimestamp(ts)),socket.inet_ntoa(ip.src),socket.inet_ntoa(ip.dst),ip.len, ip.ttl, uri_origin,os.linesep))


#     except:
#         pass

# print err

print y_test
# print y_per

# for i in range(241):
#   if y_test[i] != y_per[i]:
#       err += 1


print "error rate:%f" % (1 - err/1559.0)
print "error rate2:%f" % (err2/1336.0)

result_f.close()
process_txt.close()
list_r.close()
predict_f.close()