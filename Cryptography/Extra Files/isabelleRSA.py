import sympy
from sympy import *
import random

def choose_modulus(k,l,m):
	p1 = find_prime(k,l)
	p2 = find_prime(k,l)
	#while not (log(p1,2) + m < log(p2, 2)):
	#	p1 = find_prime(k,l)
	#	p2 = find_prime(k,l)
	#	print(p1, p2)
	print(p1, p2)
	print(log(p1,2)+m < log(p2,2))
	return p1,p2

def choose_encryption_key_old(m):
	e = random.randrange(2,m)
	while not gcd(e, totient(m)) == 1:
		e = random.randrange(2,m)
	return e

def choose_encryption_key(p1,p2):
	m = p1*p2
	e = random.randrange(2, p1*p2)
	while not gcd(e, (p1-1)*(p2-1)) == 1:
		e = random.randrange(2, p1*p2)
	return e

def compute_decryption_key(e, p1, p2):
	# d = e inverse mod phi(m) m = p1*p2
	#phi(m) = (p1-1)*(p2-1)
	d = inv_mod(e, (p1-1)*(p2-1))
	return d

def RSA_encrypt(P, e, m):
	return power_mod(P,e,m)

def RSA_decrypt(C, d, m):
	return power_mod(C,d,m)

def RSA_crack(C, e, m):
	return power_mod(C, inv_mod(e,totient(m)), m)

def power_mod(a, b, m):
	#replace with better version for large numbers
	#return ((a%m)**(b%m))%m
	return pow(a,b,m)

def string_to_int(s):
	return int.from_bytes(s.encode(),'big')

def int_to_string(n):
	return n.to_bytes((n.bit_length()+7)//8,'big').decode()

def find_prime(k, l):
	x = random.randrange(2**k+2, 2**l-1)
	while (not isprime(x)):
		x = random.randrange(2**k+2, 2**l-1)
	return x

def mod_inv_old(a,m):
	#replace with euclid's algorithm - will be using large numbers
	for i in range(0,m):
		if (i*a)%m == 1:
			return i
	return -1

def xgcd(b, n):
    """ Return g, x0, y0
        such that x0*b + y0*n = g
        and g is the gcd of (b,n)"""
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return b, x0, y0


def inv_mod(b, n):
    """ Return the modular inverse of b mod n
     or None if gcd(b,n) > 1 """
    g, x, _ = xgcd(b, n)
    if g == 1:
        return x % n