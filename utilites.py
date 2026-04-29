# Filtering of Malicious IPS

ip_list = ["10.0.0.1", "10.0.0.2", "10.0.0.3", "192.168.1.1", "172.160.1.1"]

filtered_ips = list(filter(lambda ip: ip.startswith("10.0.0"), ip_list))

print(filtered_ips)