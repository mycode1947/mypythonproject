#!/usr/bin/env python
import paramiko
f=open('/root/pythoncode/paramiko/iplist','r')
iplist=f.readlines()
f.close()
print iplist
scaniplist=map(lambda x: x.strip(),iplist)
print scaniplist
cmd="uptimee"
for ip in scaniplist:
	ssh=paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		ssh.connect(ip,username="root",timeout=2)
		stdin,stdout,stderr=ssh.exec_command(cmd,timeout=2)
		out=stdout.readlines()
		err=stderr.readlines()
		if len(out) > 0:
			print "%s is reachable over ssh" %(ip)
		elif len(err) > 0:
			print "%s is not a valid command" %(cmd)
		ssh.close()
	except:
		print "%s is not reachable" %(ip)
