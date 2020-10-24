#! /usr/bin/env python3
#! _*_ coding: utf-8 _*_
'''
本程序是一个用于处理IP地址的程序
'''
from IPy import IP, IPSet
def ip_belongs_prefix(ip_address, ip_prefix):
    #定义了一个判断IP地址是否从属于另外一个IP网段的方法
    ip_net_b = IP(ip_prefix)
    return print(ip_address in ip_net_b)
    #返回一个布尔值，如果IP地址从属于另一个网段就返回 True，如果不属于，就返回 False
def prefix_belongs_prefix(ip_prefix_1, ip_prefix_2):
    #定义了一个判断IP网段是否从属于另外一个IP网段的方法
    ip_prefix_a = IP(ip_prefix_1)
    ip_prefix_b = IP(ip_prefix_2)
    return print(ip_prefix_a in ip_prefix_b)
    #返回一个布尔值，如果IP地址从属于另一个网段就返回 True，如果不属于，就返回 False
def summary_ip(ip_prefix_times):
    #定一个使用IPSet汇总网段的方法
    ip_prefix_times = int(ip_prefix_times)
    #接收选择d后的输入的数字，并且把input中str的类型转换为int类型
    ip_list = [None] * ip_prefix_times
    #利用接收到的次数来定义列表元素的个数，用于存放输入的IP网段
    code = 0
    while code < ip_prefix_times:
        print('您第：%d 次输入的 ip 前缀，比如 192.168.1.0/24 。 您的输入是: ' % (code + 1))
        ip = input(': ')
        ip_list[code] = IP(ip)
        code = code + 1
        #使用while循环，创建列表中元素的索引，用来存放接收的IP网段
    return print(IPSet(ip_list))
    #使用IPSet求出汇总的网段
key = input('按下 y 开始本程序:  ')
while key == 'y' or key == 'Y':
    print('***************** 欢迎使用 IP Prefix 处理程序 ***************')
    print('* 按 a 开始 IP Prefix 前缀网段处理功能，列出网段详细信息    *')
    print('* 按 b 开始判断 IP 地址是否属于一个 IP 地址段               *')
    print('* 按 c 开始判断 一个 IP 地址段，是否从属于另外一个 IP 地址段*')
    print('* 按 d 启动 IP 网段地址汇总功能                             *')
    print('***********************************************')
    choose_key = input('请输入您的选择, a/b/c/d : ')
    if choose_key == 'a' or choose_key == 'A':
        print('*****  您选择了a， Prefix 前缀网段处理功能，列出网段详细信息  *****\n')
        ip_name = input('请输入IP前缀，比如 192.168.1.0/24 。您的输入是: ')
        ip_addr = IP(ip_name)
        if len(ip_addr) > 1:
            print('ip 前缀的网段为: %s' % ip_addr.net())
            print('ip 前缀子网掩码为 : %s' % ip_addr.netmask())
            print('ip 前缀广播地址为 : %s' % ip_addr.broadcast())
            print('ip 前缀的reverse : %s' % ip_addr.reverseNames()[0])
            print('ip 前缀地址个数为: %s' % len(ip_addr))
        else:
            print('hex_addr is : %s' % ip_addr.strHex)
            print('bin_addr is : %s' % ip_addr.strBin)
    elif choose_key == 'b' or choose_key == 'B':
        print('*****  您选择了b, 判断 IP 地址是否属于一个 IP 地址段   *****\n')
        ipaddress = input('请输入一个ip地址，比如 192.168.1.1 。您的输入为 : ')
        ipprefix = input('请输入一个ip网段前缀，比如 192.168.1.0/24 。您的输入为 : ')
        ip_belongs_prefix(ipaddress, ipprefix)
    elif choose_key == 'c' or choose_key == 'C':
        print('*****  您选择了c, 判断 一个 IP 地址段 是否 从属于另外一个 IP 地址段  *****\n')
        ipprefix_1 = input('请输入一个ip网段前缀，比如 192.168.1.0/24 。您的输入为 : ')
        ipprefix_2 = input('请输入另外一个ip网段前缀，比如 192.168.0.0/16 。您的输入为 : ')
        prefix_belongs_prefix(ipprefix_1, ipprefix_2)
    elif choose_key == 'd' or choose_key == 'D':
        print('*****  您选择了d, 启动 IP 网段地址汇总功能  *****\n')
        summary_prefix = input('请输入您要汇总网段的数量，比如您要汇总5个网段，就输入5. 您的选择是 : ')
        summary_ip(summary_prefix)
    else:
        print('没有这个选项 , 请在 a,b,c,d 的四个选项中选择')
    print('*****  继续使用本程序，青按字母 y 退出本程序，请按字母 n 或者其他键 *****')
    key = input('继续本程序 或 退出本程序 Y/N : ')