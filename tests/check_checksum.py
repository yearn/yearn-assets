import os
import eth_utils

base = "icons"


def checksum_encode(addr):
    # from https://github.com/ethereum/EIPs/blob/master/EIPS/eip-55.md
    hex_addr = addr.hex()
    checksummed_buffer = ""
    hashed_address = eth_utils.keccak(text=hex_addr).hex()
    for nibble_index, character in enumerate(hex_addr):
        if character in "0123456789":
            checksummed_buffer += character
        elif character in "abcdef":
            hashed_address_nibble = int(hashed_address[nibble_index], 16)
            if hashed_address_nibble > 7:
                checksummed_buffer += character.upper()
            else:
                checksummed_buffer += character
    return "0x" + checksummed_buffer


def test(addr_str):
    addr_bytes = eth_utils.to_bytes(hexstr=addr_str)
    checksum_encoded = checksum_encode(addr_bytes)
    return checksum_encoded == addr_str, addr_str, checksum_encoded


def main():
    checks = []
    for root, dirs, files in os.walk(base):
        names = dirs + files
        for name in names:
            if name.startswith("0x") and len(name) == 42:
                correct, got, expected = test(name)
                if not correct:
                    checks.append((got, expected))
    if len(checks) != 0:
        for got, expected in checks:
            print(f"Error: got {got}, expected {expected}.")
        exit(1)


if __name__ == "__main__":
    main()
