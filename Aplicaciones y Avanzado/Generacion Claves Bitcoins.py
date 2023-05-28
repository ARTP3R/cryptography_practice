import ecdsa
import random
import hashlib

b58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def privateKeyToWif(key_hex):    
    return base58CheckEncode(b'\x80', bytes.fromhex(key_hex))
    
def privateKeyToPublicKey(s):
    sk = ecdsa.SigningKey.from_string(bytes.fromhex(s), curve=ecdsa.SECP256k1)
    vk = sk.verifying_key
    return ('\04' + sk.verifying_key.to_string().hex())
    
def pubKeyToAddr(s):
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(hashlib.sha256().digest())
    return base58CheckEncode(b'\x00',ripemd160.digest())

def keyToAddr(s):
	return pubKeyToAddr(privateKeyToPublicKey(s))

def base58encode(n):
    result = ''
    while n > 0:
        result = b58[n%58] + result
        n /= 58
    return result

def base58CheckEncode(version, payload):
    s = version + payload
    checksum = hashlib.sha256(hashlib.sha256(s).digest()).digest()[0:4]
    result = s + checksum
    leadingZeros = countLeadingChars(result, '\0')
   
    return '1' * leadingZeros + base58encode(base256decode(result))

def base256decode(s):
    result = 0
    for c in s:
        result = result * 256 + c
    return result

def countLeadingChars(s, ch):
    count = 0
    for c in s:
        if c == ch:
            count += 1
        else:
            break
    return count

private_key = ''.join(['%x' % random.randrange(16) for x in range(0, 64)])
print ('Private key: ' + private_key)
pubKey = privateKeyToPublicKey(private_key)
print ('Public key: ' + pubKey)
print ('Wif: ' + privateKeyToWif(private_key))
print ('Address: ' + keyToAddr(private_key))