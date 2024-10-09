#!/usr/bin/python
import socket
from binascii import hexlify
import sys
from optparse import OptionParser
from pylibpcap.base import Sniff

def host2str(host):
    packed_ip_addr = socket.inet_aton(host)
    hexStr = hexlify(packed_ip_addr)
    return hexStr.decode("utf-8")

if __name__ == "__main__":
    usage = '''usage: %prog [options]
It is a script which is used to capture vxlan packet'''
    parser = OptionParser(usage)
    parser.add_option("-s", "--src", dest="src_host",
                      help="inner src host to filter")
    parser.add_option("-d", "--dst", dest="dst_host",
                      help="inner dst host to filter")
    parser.add_option("--device", dest="device", default="eth0",
                      help="device to listen on")
    options, _ = parser.parse_args()
    device = options.device

    if not options.src_host and not options.dst_host:
        parser.print_help()
        sys.exit(1)

    packet_accesor = ""
    if options.src_host:
        hexStr = host2str(options.src_host)
        packet_accesor += "ether[76:4]=" + "0x" + hexStr

    if options.dst_host:
        hexStr = host2str(options.dst_host)
        if packet_accesor:
            packet_accesor += " and " + "ether[80:4]=" + "0x" + hexStr
        else:
            packet_accesor += "ether[80:4]=" + "0x" + hexStr

    sniffobj = None
    try:
        sniffobj = Sniff(device, count=100, promisc=1, filters=packet_accesor, timeout=10)
        for plen, t, buf in sniffobj.capture():
            if plen:
                print("[+]: Payload len=", plen)
                print("[+]: Time", t)
                print("[+]: Payload", buf)
    except KeyboardInterrupt:
        pass
    except LibpcapError as e:
        print(e)
        exit(1)

    if sniffobj is not None:
        stats = sniffobj.stats()
        print("\n")
        print(stats.capture_cnt, " packets captured")
        print(stats.ps_recv, " packets received by filter")
        print(stats.ps_drop, " packets dropped by kernel")
        print(stats.ps_ifdrop, " packets dropped by iface")


