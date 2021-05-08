import scapy.all as scapy
from scapy_http import http
import optparse

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", help="Enter Interface")
    option = parse_object.parse_args()[0]
    if not option:
        print("Enter interface")
    return option

def listen_packets(interface):
    scapy.sniff(iface=interface, store=False, prn=analyze_packets)

def analyze_packets(packet):
    #packet.show()
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)

iface = get_user_input().interface
listen_packets(iface)

