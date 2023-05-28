#XOR de datos binarios
def xor_data(binary_data_1, binary_data_2):
    return bytes([b1 ^ b2 for b1, b2 in zip(binary_data_1, binary_data_2)])

m1 = bytes('España','utf-8')
m = bytes("keepcoding===","utf-8")
k = bytes("abcdefghijddd","utf-8")

#m ^k = dato

print(xor_data(m,k))
print(xor_data(m,k).hex())
#=====
print(xor_data(k,m).hex())

# K1 (key manager) ^ K2 (desarrollador) = K (keyStore)
# 123456 (IT) ^ 234563 (desarrollo) = Kd 

#K2 = K ^ K1; K1 = K ^ K2