echo "----------------------------------------------------------"
echo "			Blocked Log				"
echo "----------------------------------------------------------"
cat /var/log/iptables/iptables.blocked.log | /usr/bin/python2.7 /usr/local/bin/parse-iptlog.py
echo "Press enter to read allowed log"
read
echo "----------------------------------------------------------"
echo "			Allowed Log				"
echo "----------------------------------------------------------"
cat /var/log/iptables/iptables.allowed.log |  /usr/bin/python2.7 /usr/local/bin/parse-iptlog.py
