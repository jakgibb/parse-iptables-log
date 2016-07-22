# parse-iptables-log

Very quick fix to prettifying iptables logs.  
Outputting them in a more friendly way and giving a short summary on the top IP/port hits.  

Edited example:
![Edited Example](https://i.imgur.com/lRSRJOO.png)

Expects your log daemon to send blocked and allowed requests to different log files.  
Example with rsyslog:  
> :msg, contains, "iptblock" -/var/log/iptables/iptables.blocked.log  
> :msg, contains, "iptallow" -/var/log/iptables/iptables.allowed.log  
> & ~

#Usage
Pipe the logs to parse-iptlog.py, or adjust the view-ipt-log.sh script with the log locations and execute it which will pipe it to the Python script for you.
