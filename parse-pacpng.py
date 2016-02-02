from pcapng import FileScanner
import os

# # with open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/4.pcapng') as fp:
# fp_r =  open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/4.pcapng','r')
# scanner = FileScanner(fp)
# for block in scanner:
#     print block
#     num = raw_input('enter y/n:')
#     if num = 'y':
#     	print block
#     else:
#     	pass
# fp.close



fp_w = open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/test.txt','a')
fp_r =  open('/home/jimlee/Documents/Git/simple-sql-inject-pacpng-detection-by-SVM/4.pcapng','r')
scanner = FileScanner(fp_r)
i = 0
for block in scanner:
	# i += 1
	# if i > 2:
    fp_w.write("%s%s" % (block ,os.linesep))
    # else:
    # 	continue
fp_w.close
fp_r.close
