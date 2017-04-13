#!/usr/bin/env python
import paramiko
class Servers(object):
	def __init__(self,hostname,cmd):
		self.hostname=hostname
		ssh=paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(hostname,username="root",password="redhat")
		stdin,stdout,stderr=ssh.exec_command(cmd)
		print stdout.readlines()
		ssh.close()
	def checkuptime(self,hostname):
		ssh=paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(hostname,username="root",password="redhat")
		stdin,stdout,stderr=ssh.exec_command("uptime")
		print stdout.readlines()
		ssh.close()
class moreinfo(Servers):
	def __init__(self,hostname):
		self.hostname=hostname
		print "Will be verifying the host %s" %(self.hostname)
	def checkdatetime(self,hostname):
		ssh=paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(hostname,username='root',password='redhat')
		stdin,stdout,stderr=ssh.exec_command('date')
		print stdout.readlines()
		ssh.close()
