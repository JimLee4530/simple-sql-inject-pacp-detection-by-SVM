import re
import dpkt
import sys
import os
import urllib

# f_pcap = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/cap_00008_20141129084512.pcap',"r")
# f_w = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/nomaltext_process.txt',"w")
f_w = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/testSetProcess.txt',"w")
# f_w = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/nomaltext_process.txt',"a")
f_r = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/testSet(1:223,0:1336).txt','r')

for uri in f_r.readlines():
    # uri = http.uri
    uri = uri.lower()
    uri = re.sub(r'(http|https)://[^\s]*', ' httpaddr ', uri)
    uri = re.sub(r'\?', ' question_mask ', uri)
    uri = re.sub(r'\/',' backslash ', uri)
    uri = re.sub(r'\%', ' per_cent ', uri)
    uri = re.sub(r'\-', ' hyphen ', uri)
    uri = re.sub(r'\'', ' colon ', uri)
    uri = re.sub(r'\=', ' equality_sign ', uri)
    uri = re.sub(r'\(', ' left_bracket ', uri)
    uri = re.sub(r'\)', ' right_bracket ', uri)
    uri = re.sub(r'\&',' and_mask ',uri)
    uri = re.sub(r'[0-9]+', ' number ', uri)
    uri = re.sub(r'\~', ' wave_number ', uri)
    uri = re.sub(r'\*', ' multiplication_sign ', uri)
    uri = re.sub(r'\#', ' note_sign ', uri)
    uri = re.sub(r'\<', ' left_angle_bracket ', uri)
    uri = re.sub(r'\>', ' right_angle_bracket ', uri)
    uri = re.sub(r'\@', ' at_sign ', uri)
    uri = re.sub(r'\+', ' add_sign ', uri)
    uri = re.sub(r'\;', ' semicolon ', uri)
    uri = re.sub(r'\{', ' left_curly_braces ', uri)
    uri = re.sub(r'\}', ' right_curly_braces ', uri)
    uri = re.sub(r'\!', ' exclamation_mark ', uri)
    uri = re.sub(r'\|', ' bit_or ', uri)
    f_w.write('%s' % (urllib.unquote(uri)))

f_w.close()

# pcap = dpkt.pcap.Reader(f_pcap)
# for ts, buf in pcap:
#     # print ts,len(buf)
#     try:
#         eth = dpkt.ethernet.Ethernet(buf)
#         ip = eth.data
#         tcp = ip.data

#     # print tcp.sport
#     # print tcp.dport
    	
#         if tcp.dport == 80 and len(tcp.data) > 0:
#             http = dpkt.http.Request(tcp.data)
#             # print http.method
#             uri = http.uri
#             uri = uri.lower()
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
#             f_w.write('%s%s' % (urllib.unquote(uri),os.linesep))
#         	# print http.version
#         	# print http.headers
#     except:
#         pass


# f_pcap.close()
# f_w.close()


# f_pcap = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/5.pcap',"r")
# pcap = dpkt.pcap.Reader(f_pcap)
# for ts, buf in pcap:
#     # print ts,len(buf)
#     try:
#         eth = dpkt.ethernet.Ethernet(buf)
#         ip = eth.data
#         tcp = ip.data
#         if tcp.dport == 80 and len(tcp.data) > 0:
#             http = dpkt.http.Request(tcp.data)
#             uri = http.uri
#             f_w.write('%s%s' % (urllib.unquote(uri),os.linesep))
#     except:
#         pass
# f_pcap.close()

# for i in range(1,9):
#     f_pcap = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/cap_0000%i.pcap' % (i),'r')
#     pcap = dpkt.pcap.Reader(f_pcap)
#     for ts, buf in pcap:
#     # print ts,len(buf)
#         try:
#             eth = dpkt.ethernet.Ethernet(buf)
#             ip = eth.data
#             tcp = ip.data

#             if tcp.dport == 80 and len(tcp.data) > 0:
#                 http = dpkt.http.Request(tcp.data)
#                 uri = http.uri

#                 f_w.write('%s%s' % (urllib.unquote(uri),os.linesep))
#         except:
#             pass

#     f_pcap.close()

# f_w.close()