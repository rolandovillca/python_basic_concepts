#!/usr/bin/env python3
import datetime
import time
import os
import psutil
from pssh.clients import ParallelSSHClient
# This script runs assumes the output of .rss is in bytes

user = "em7admin"
password = "em7admin"
host_count = 1000

start = time.time()
process = psutil.Process(os.getpid())

def print_e(msg = ""):
    elapsed = time.time() - start
    cur_time = datetime.datetime.now().strftime("%d %b %H:%M:%S")
    mem_usage = int(process.memory_info().rss // 1024) / 1024.0
    out_str = "{} ({:.2f}MiB/{:.4f}s): {}".format(cur_time, mem_usage, elapsed, msg)
    print(out_str, flush=True)

print_e("Starting Up")



print_e("Creating hosts list")
hosts = []
for i in range(host_count):
    hostname = "test-host{}".format(i)
    hosts.append(hostname)

    ##Print out format for /etc/hosts
    #print("::1\t{}".format(hostname))

hosts = ['10.2.6.19', '10.2.6.20', '10.2.6.26', '10.2.6.52']

print_e("Creating ssh client")
client = ParallelSSHClient(hosts, user=user, password=password)
print_e("Executing run command: ls")
output = client.run_command('ls')

"""
hostc = 0
linec = 0
charc = 0 
print_e("Reading output of cmd 1")
for host, host_out in output.items():
    hostc += 1
    for line in host_out.stdout:
        linec += 1
        charc += len(line)
        #print(line)

print_e("Executing run command: whoami")
output = client.run_command('whoami')

print_e("Reading output of cmd 2")
for host, host_out in output.items():
    hostc += 1
    for line in host_out.stdout:
        linec += 1
        charc += len(line)

print_e("Executing run command: ps aux")
output = client.run_command('ps aux')

print_e("Reading output of cmd 3")
for host, host_out in output.items():
    hostc += 1
    for line in host_out.stdout:
        linec += 1
        charc += len(line)

print_e("Executing run command: netstat -tp")
output = client.run_command('netstat -tp')

print_e("Reading output of cmd 4")
for host, host_out in output.items():
    hostc += 1
    for line in host_out.stdout:
        linec += 1
        charc += len(line)


print_e("Complete")
print("\n\n=======================\nTotal stats\n=======================")
print("Total hosts: {}".format(len(hosts)))
print("Hosts responses (total for all commands): {}".format(hostc))
print("Total Lines: {}".format(linec))
print("Total Characters: {}".format(charc))
"""