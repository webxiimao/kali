# -*- coding: utf-8 -*-
from scapy.all import get_if_hwaddr


interface = raw_input('请输入网卡名')
mac =get_if_hwaddr(str(interface))

print mac
