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


process_txt = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/nomaltext_process.txt',"r")
# f_w = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/nomaltext_process.txt',"w")
# f_X = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/X.txt',"w")
# f_y = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/y.txt',"w")

list_r = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/key_list.txt','r')
key_list=[]
all_lines = list_r.readlines()
for each_line in all_lines:
    key_list.append(each_line.strip())
# print len(key_list)

X = np.zeros([567,len(key_list)],int)
y = np.hstack([np.ones([236],int),np.zeros([331],int)])

n = 0

all_lines = process_txt.readlines()
for each_line in all_lines:
	txt_array = string.split(each_line,' ')
	# print txt_array 
	# raw_input('pause')
	for i in range(0, len(txt_array)):
        # print txt_array[i]
        # print 
		for j in range(0,len(key_list)):
            # print txt_array[i]
            # print len(key_list)
            # print X[n,j]
			if txt_array[i] == key_list[j]:
				X[n,j] = 1
	n = n + 1



#================================Support Vector Machine================================


h = 0.02

C = 1.0
svc = svm.SVC(kernel='linear',C=C).fit(X,y)
rbf_svc = svm.SVC(kernel='rbf',gamma=0.7,C=C).fit(X,y)
poly_svc = svm.SVC(kernel='poly',degree=3,C=C).fit(X,y)
lin_svc = svm.LinearSVC(C=C).fit(X,y)


#==============================Predict=========================================
predict_f = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/4.pcap',"r")
predict_pcap = dpkt.pcap.Reader(predict_f)

result_f = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/result.txt',"w")

X_pre = np.zeros([1,len(key_list)],int)

for ts, buf in predict_pcap:
    # print ts,len(buf)
	eth = dpkt.ethernet.Ethernet(buf)
	ip = eth.data
	tcp = ip.data
	
    # print tcp.sport
    # print tcp.dport

#===============================bebug part===================================
	try:
		if tcp.dport == 80 and len(tcp.data) > 0:
			http = dpkt.http.Request(tcp.data)
            # print http.method
			uri_origin = http.uri
			uri = uri_origin.lower()
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
            # f_w.write('%s%s' % (urllib.unquote(uri),os.linesep))
            # print http.version
            # print http.headers
		# print X_pre
		# print svc.predict(X_pre) #svc isn't work!
			result = rbf_svc.predict(X_pre) #rbf is work!
		# print poly_svc.predict(X_pre)  # poly isn't work!
		# print lin_svc.predict(X_pre) #lin isn't work!
			print http.uri
			if result == 1:
				# print X_pre
				# print 'IP:%s-->%s' % (socket.inet_ntoa(ip.src),socket.inet_ntoa(ip.dst))
				# print urllib.unquote(http.uri)
				# print str(datetime.datetime.utcfromtimestamp(ts))
				result_f.write('%s\nIP:%s-->%s   (len=%d ttl=%d) \n dangerous data : %s %s' % (str(datetime.datetime.utcfromtimestamp(ts)),socket.inet_ntoa(ip.src),socket.inet_ntoa(ip.dst),ip.len, ip.ttl, uri_origin,os.linesep))


	except:
		pass

result_f.close()
process_txt.close()
list_r.close()
predict_f.close()