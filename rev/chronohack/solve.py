from pwn import *
import random
import time
import socket
# only get time initially and adjust from there not each time.
def get_random(length, seed):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    random.seed(seed)  
    s = ""
    for i in range(length):
        s += random.choice(alphabet)
    return s

def main():
        HOST = "verbal-sleep.picoctf.net"
        PORT = 57979 
        for i in range(0, 5000):
            if (i % 50 == 0):
                p = remote(HOST,PORT)
                seed = (int(time.time() * 1000))
            token = get_random(20, seed + i)
            print(f"token: {token}")        
            p.recvuntil(b"(or exit):")            
            p.sendline(token.encode())
            response = p.recvuntil(b"\n")
            if b"Congratulations" in response:
                print(p.recvuntil(b"}"))
                exit()

main()


