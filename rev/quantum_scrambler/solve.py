from pwn import *

def main():
    HOST = "verbal-sleep.picoctf.net"
    PORT = 52453
    p = remote(HOST, PORT)
    input = p.recvall().decode()
    lists = eval(input)
    print(f"flag len: {len(lists)*2}")
    # we need the first and last hex char in each element of
    # the lists outputted from eval

    # im missing 2 characters since my current len is 30 not 32 so I need to manipualte the finals element in lists somehow, check source
    flag = ""
    for each in lists: 
        flag += chr(int(each[0],16))
        flag += chr(int(each[-1],16))        
        print(flag)

main()
