# Convert hex to base64
# The string: 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
# Should produce: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
#
from binascii import b2a_base64

hexString = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

# Get byte representation of hex string 
bytesOfHexString = bytes.fromhex(hexString)

#base64 encode hex string bytes
base64RepOFHexBytes = b2a_base64(bytesOfHexString)

#Print base64 rep of Hex string with no new line
print(base64RepOFHexBytes.rstrip())

