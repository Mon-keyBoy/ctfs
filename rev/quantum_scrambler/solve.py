from pwn import *

def main():
    HOST = "verbal-sleep.picoctf.net"
    PORT = 52453
    p = remote(HOST, PORT)
    input = p.recvall().decode()
    #print(input)
    lists = eval(input)
    #print(f"flag len: {len(lists)*2}")
    
    flag = ""
    for each in lists[:-2]: 
        flag += chr(int(each[0],16))
        flag += chr(int(each[-1],16))        
    # bc they start at 2 for scrambling the last 2 elements we only take the first and not the first AND last char of
    for each in lists[-2:]:
        flag += chr(int(each[0],16))
    print(flag)

main()
