echo "----------------------------------------------------------"
echo "			Blocked Log				"
echo "----------------------------------------------------------"
/usr/bin/python2.7 /usr/local/bin/parse-iptlog.py < /var/log/iptables/iptables.blocked.log
echo "Press enter to read allowed log"
read
echo "----------------------------------------------------------"
echo "			Allowed Log				"
echo "----------------------------------------------------------"
/usr/bin/python2.7 /usr/local/bin/parse-iptlog.py < /var/log/iptables/iptables.allowed.log
