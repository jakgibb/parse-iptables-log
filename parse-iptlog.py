import re
import fileinput
from collections import Counter

pair_re = re.compile('([^ ]+)=([^ ]+)')
portlist = []
iplist = []

for line in fileinput.input():
    line = line.rstrip()
    data = dict(pair_re.findall(line))
    date = line.split()
    portlist.append(data['DPT'])
    iplist.append(data['SRC'])
    print date[0]+" "+date[1]+" "+date[2]+" ",
    print data['PROTO'], "\tDPT:", data['DPT'], "\tSPT:", data['SPT'], "\tSRC:", data['SRC'], "\tDST:", data['DST']

try:
    print "\n"
    count = 0
    linesToShow = 10
    while (count < linesToShow):
        portcommon = [ite for ite, it in Counter(portlist).most_common()]
        print "Port: "+str(portcommon[count])+" had "+str(portlist.count(portcommon[count]))+" hits"
        count = count + 1

except IndexError:
    print ""

try:
    print "\n"
    count = 0
    while (count < linesToShow):
        ipcommon = [ite for ite, it in Counter(iplist).most_common()]
        print "IP: "+str(ipcommon[count])+" had "+str(iplist.count(ipcommon[count]))+" hits"
        count = count + 1
except IndexError:
    print ""
print "\n"
