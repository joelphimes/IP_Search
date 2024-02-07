import ipaddress

# Function to check if an IP is in the specified /24 subnet
def is_in_subnet(ip, subnet):
    return ipaddress.ip_address(ip) in ipaddress.ip_network(subnet, strict=False)

# Specify the /24 subnet you want to check against
subnet_24 = '192.168.1.0/24'

# Open the file containing the IP addresses
with open('ips.txt', 'r') as file:
    for line in file:
        ip = line.strip()  # Remove any leading/trailing whitespace
        try:
            # Check if IP is a valid single address (/32)
            if ipaddress.ip_network(ip, strict=False).prefixlen == 32:
                print(f'{ip} is in a /32 range')
            # Check if IP is in the specified /24 subnet
            elif is_in_subnet(ip, subnet_24):
                print(f'{ip} is in the specified /24 range ({subnet_24})')
            else:
                print(f'{ip} is neither in a /32 range nor in the specified /24 range ({subnet_24})')
        except ValueError:
            print(f'{ip} is not a valid IP address')