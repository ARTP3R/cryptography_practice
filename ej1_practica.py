#!/usr/bin/env python3

# A1EF2ABFE1AAEEFF
# B1AA12BA21AABB12

b1 = bytes.fromhex('A1EF2ABFE1AAEEFF')
b2 = bytes.fromhex('B1AA12BA21AABB12')

b3 = (b1 ^ b2)
b3_hex = (b1 ^ b2).hex()

print("b3=b1^b2: ", b3_hex)

b22 = (b3 ^ b1)

print("b2=b3 ^b1: ", b22.hex())

b11= (b2 ^ b3)

print("b1=b2 ^b3: ", b11.hex())
