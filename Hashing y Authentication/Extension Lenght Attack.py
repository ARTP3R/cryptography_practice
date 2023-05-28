import hashpumpy
import hashlib
import sys

password=b'password'
message= b'mensaje'
addition = b'comprometido'

if (len(sys.argv)>1):
  password=(sys.argv[1]).encode()
if (len(sys.argv)>2):
  message=(sys.argv[2]).encode()
if (len(sys.argv)>3):
  addition=(sys.argv[3]).encode()


# Calculo del hash original tal que H(Password || Message)
m = hashlib.sha1()
m.update((password+message))
rtn=m.hexdigest()
print ("Hash original: ",rtn)


# Calculamos un  hash for H(Password || Message || Addition)
rtn = hashpumpy.hashpump(rtn, message, addition, len(password))

print ("Nuevo hash: ",rtn[0])
print ("Nuevo message: ",rtn[1])

m = hashlib.sha1()
m.update(password+rtn[1])
rtn=m.hexdigest()
print ("Calculamos nuevo hash con los siguientes datos (password+newdata): ",rtn)

