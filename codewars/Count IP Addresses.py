from ipaddress import IPv4Address


def ips_between(first: str, last: str) -> int:
    first_address = int(IPv4Address(first))
    last_address = int(IPv4Address(last))
    return last_address - first_address - 1
