import re
import dpkt
import sys
import os
import urllib

f_r = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/cap_00001_20141129084421.pcap',"r")
f_w = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/nomaltext_process.txt',"a")

pcap = dpkt.pcap.Reader(f_r)
for ts, buf in pcap:
    # print ts,len(buf)
    try:
    	eth = dpkt.ethernet.Ethernet(buf)
    	ip = eth.data
    	tcp = ip.data

    # print tcp.sport
    # print tcp.dport
    	
        if tcp.dport == 80 and len(tcp.data) > 0:
        	http = dpkt.http.Request(tcp.data)
        	# print http.method
        	uri = http.uri
        	uri = uri.lower()
        	uri = re.sub(r'(http|https)://[^\s]*', ' httpaddr ',uri)
        	uri = re.sub(r'%', ' ',uri)
        	uri = re.sub(r'\/\?', ' ',uri)
        	uri = re.sub(r'\/','',uri)
        	uri = re.sub(r'\=',' ',uri)
        	uri = re.sub(r'\&',' ',uri)
        	uri = re.sub(r'[0-9]+', ' number ', uri)  
        	uri = re.sub(r'\-', ' ',uri)
        	f_w.write('%s%s' % (urllib.unquote(uri),os.linesep))
        	# print http.version
        	# print http.headers
    except:
        pass


f_r.close()
f_w.close()