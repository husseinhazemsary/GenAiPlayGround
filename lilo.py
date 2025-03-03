import psutil

def get_network_info():
    interfaces = psutil.net_if_addrs()
    for interface, addresses in interfaces.items():
        print(f"\nInterface: {interface}")
        for address in addresses:
            if address.family == 2:  # IPv4
                print(f"  IPv4 Address: {address.address}")
            elif address.family == 23:  # IPv6
                print(f"  IPv6 Address: {address.address}")
            elif address.family == 17:  # MAC Address
                print(f"  MAC Address: {address.address}")

if __name__ == "__main__":
    print("Fetching network details...\n")
    get_network_info()
