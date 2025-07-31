from pwn import *

# nc connect shit
def conn():
    return remote("verbal-sleep.picoctf.net", 52468)
global p

p = conn()

# my funcs for this solve

# get encrypted text from plaintext word
def encrypt(word):
    p.recvuntil("do?")
    p.sendline("e")
    p.recvuntil("encrypt?")
    p.sendline(word)
    p.recvuntil("cheese:  ")
    return p.recvuntil("\n").strip().decode()

def uncapAscii(char):
    return (ord(char.upper()) - ord('A'))

def doMath(ptc1, enc1, ptc2, enc2):
    # solve for a
    xdiff = ptc1 - ptc2
    ediff = enc1 - enc2
    # pow(xdiff, -1, 26) is the modular inverse
    a = ((ediff * pow(xdiff, -1, 26)) % 26)
    # solve for b
    b = ((enc1 - (a * ptc1)) % 26)
    return a, b


def decWord(word, a, b):
    decStr = ""
    for char in word:
        # decrypt func is
        # (inva*(enc - b)) % 26
        decStr += chr(((pow(a, -1, 26)*(uncapAscii(char) - b)) % 26)+ord('A'))
    return decStr



# send payload

# seems like it won't accept non-cheese words
p.recvuntil("it:  ")
# get rid of new line and make str from bytes
encFlag = p.recvuntil("\n").strip().decode()

encWord = encrypt("cheddar")

a, b = doMath(uncapAscii('C'), uncapAscii(encWord[0]), uncapAscii('H'), uncapAscii(encWord[1]))

decFlag = decWord(encFlag, a, b)
print(decFlag)


p.interactive()

# an affine cipher is
# ax + b % 26 = ordChar
# so to reverse this we take the modular inverse
# the math for this is that we brute every number in the
# modular 26 range and multiply that by our x
# whichever number leaves a module of 1 is a
# ex to get the modular inverse of 3x % 26 = ordChar
# since ordChar is just a remainder we 
# would brute x until we find a number that gives ordChar

# to sovle the cypher we need a and b, so first make two 
# functions and take out b (x is the plaintextchar)
# ax + b % 26 = enc1 ax + b % 26 = enc2
# a % 26 = (enc1 - enc2)/(x1-x2) % 26
# we need to find the modular inverse of both of those though

