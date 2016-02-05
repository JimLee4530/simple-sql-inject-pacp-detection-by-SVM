
              
import dpkt
import sys
import os
import urllib

f=open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/5.pcap',"r")
f_w=open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/test.txt',"w")
pcap=dpkt.pcap.Reader(f)


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
            f_w.write('%s%s' % (urllib.unquote(http.uri),os.linesep))
            # print http.version
            # print http.headers
    except:
        pass

    # raw_input()


f.close()
f_w.close()