import sys
from random import randint

# Alicia a y Bernardo b
# (0,0) -> 0-10 , (0,1) -> 10-20, (1,0) -> 20-30, (1,1) -> mayor de 30 
a_0 = 1 
a_1 = 0
b_0 = 1
b_1 = 0

def inv(val):
	return(val ^ 1)
	
r1 =randint(1, 5)
r2= randint(1, 5)
r3 =randint(1, 5)
r4 =randint(1, 5)

q1 =randint(50000, 60000)
q2 =randint(50000, 60000)
q3 =randint(50000, 60000)
q4 =randint(50000, 60000)


p =randint(10000, 20000)


c_bit_a_0 =  q1 * p + 2*r1 +a_0
c_bit_a_1 =  q2 * p + 2*r2 +a_1 
c_bit_b_0 =  q3 * p + 2*r3 +b_0 
c_bit_b_1=  q4 * p + 2*r4 +b_1

# Truth table

cipher_older = inv(c_bit_a_1)*c_bit_b_1 + inv(c_bit_a_1)*inv(c_bit_a_0)*c_bit_b_0  + inv(c_bit_a_0)*c_bit_b_1*c_bit_b_0


			
print("r values:\t",r1,r2,r3,r4)
print("q values:\t",q1,q2,q3,q4)
print("p value:\t",p)

print("\nInput bits")
print("---------------")
print("a_1:\t",a_1, "a_0:\t",a_0)
print("b_1:\t",b_1, "b_0:\t",b_0)

print("\nCipherbits")
print("---------------")
print("a:\t",c_bit_a_0, "b:\t",c_bit_a_1)
print("c:\t",c_bit_b_1, "d:\t",c_bit_b_1)

print("\nCipher result")
print("---------------")
print("Result:\t",cipher_older)

#decrypt
result = (cipher_older % p) % 2

print("\nResults")
print(result)
if (result==1):
	print("Bob is older than Alice")
else:
	print("Bob is not older than Alice")
