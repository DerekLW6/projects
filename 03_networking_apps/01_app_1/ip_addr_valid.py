from IPy import IP  

# String function 
def ip_addr_valid(ip_list): 
    correct_ips = []
    for ip in ip_list:
        a = ip.split('.')

        if len(a) != 4:
            ip_list.pop(a)
        else:
            value = IP(ip)
            correct_ips.append(value.strNormal())

    return correct_ips
    
