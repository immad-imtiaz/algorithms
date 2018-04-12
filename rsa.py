
from fractions import gcd
p=7
q=13
n=p*q
phi = (p-1)*(q-1)
all_possible = []
for i in range(1, phi-1):
    g_cd =gcd(i, phi)
    if g_cd == 1:
        all_possible.append(str(i))

# Code for Eucledian GCD
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

for i in all_possible:
    inv = modinv(int(i), phi)
    print('('+str(i) + ',' + str(inv) + ')')
