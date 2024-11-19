import argparse
import binascii
import re

# Get command line argument and validate hex value
parser = argparse.ArgumentParser()
parser.add_argument('hex_val', help='Hex value of SIP you want in format 0xNNN')
args = parser.parse_args()

# Regex pattern to validate 0xNNN format
hex_pattern = re.compile(r'^0x[0-9A-Fa-f]{1,3}$')
if not hex_pattern.match(args.hex_val):
    raise ValueError('Argument must be in format 0xNNN where N is a hex digit')

# Remove 0x prefix for further processing
input_string = args.hex_val[2:]

def hexswap(input_hex: str):
    hex_pairs = [input_hex[i : i + 2] for i in range(0, len(input_hex), 2)]
    hex_rev = hex_pairs[::-1]
    hex_str = "".join(["".join(x) for x in hex_rev])
    return hex_str.upper()

def string_to_hex(input_string):
    if not (len(input_string) % 2) == 0:
        input_string = "0" + input_string
    input_string = hexswap(input_string)
    input_string = binascii.unhexlify(input_string)
    input_string = input_string.ljust(4, b'\x00')
    return str(input_string.hex()).upper()

print("csr-active-config should be: ", string_to_hex(input_string))
