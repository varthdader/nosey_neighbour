#!/usr/bin/python

import sys, os, time
target = str(sys.argv[1])

def smb_windows_share():
	cmd600 = 'enum4linux -a -M -l ' + target + ' |tee enum4linux.txt'
	cmd601 = 'smbmap -H ' + target + ' -P 139 | tee smbmap.txt'
	cmd602 = 'smbmap -H ' + target + ' -P 139 -R | tee smbmap.txt'
	cmd603 = 'smbclient -L\\ -N -I ' + target + '| tee smbclient.txt'
	print '[+] Running Windows Share Enumeration... '
	os.system(cmd600)
	os.system(cmd601)
	os.system(cmd602)
	os.system(cmd603)

def smb_windows_domain():
	cmd610 = 'enum4linux -a -M -l ' + target + ' |tee enum4linux.txt'
	cmd611 = 'smbmap -H ' + target + ' -P 445 | tee smbmap.txt'
	cmd612 = 'smbmap -H ' + target + ' -P 445 -R | tee smbmap.txt'
	cmd613 = 'smbmap -H ' + target + ' -P 445 -x "ipconfig /all" | tee smbmap.txt'
	cmd613 = 'smbclient -L\\ -N -I ' + target + ' | tee smbclient.txt'
	print '[+] Running Windows Domain Enumeration... '
	os.system(cmd610)
	os.system(cmd611)
	os.system(cmd612)
	os.system(cmd613)

def smb_windows_rpc():
	cmd620 = 'sslscan --show-certificate --no-colour ' + target
	cmd621 = 'rcpclient -U "" ' + target + ' -c "srvinfo;enumdomusers;getdompwinfo;querydominfo;netshareenum;netshareenumall"
	print '[+] Running Windows RPC Enumeration... '
	os.system(cmd620)
	
