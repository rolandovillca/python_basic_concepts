'''
If you want to determine in a local network which addresses are active or which
computers are active, this script can be used. But you have to be careful with
the range, because it can jam the network, if too many pings are started at once.

Manually we would do the following for a network 192.168.178.x: We would ping
the addresses 192.168.178.0, 192.168.178.1, 192.168.178.3 until 192.168.178.255
in turn. Every time we would have to wait a few seconds for the return values.
This can be programmed in Python with a for loop over the address range of the
IP addresses and a os.popen("ping -q -c2 "+ip,"r").
'''

import os, re, threading

class ip_check(threading.Thread):
    def __init__ (self,ip):
        threading.Thread.__init__(self)
        self.ip = ip
        self.__successful_pings = -1
    def run(self):
        ping_out = os.popen("ping -q -c2 "+self.ip,"r")
        while True:
            line = ping_out.readline()
            if not line: break
            n_received = re.findall(received_packages,line)
            if n_received:
                self.__successful_pings = int(n_received[0])
    def status(self):
        if self.__successful_pings == 0:
            return "no response"
        elif self.__successful_pings == 1:
            return "alive, but 50 % package loss"
        elif self.__successful_pings == 2:
            return "alive"
        else:
            return "shouldn't occur"

received_packages = re.compile(r"(\d) received")

check_results = []
for suffix in range(20,70):
    ip = "192.168.178."+str(suffix)
    current = ip_check(ip)
    check_results.append(current)
    current.start()

for el in check_results:
    el.join()
    print "Status from ", el.ip,"is",el.status()