from pwn import *
import re


def get_inputs():
    HOST = "verbal-sleep.picoctf.net"
    POST = 52453
    p = remote(HOST, POST)
    return p.recvall().decode()

def hex_to_chrs(istring):
    # this don't work because re.sub takes precedent over the int call kmskmskms
    # for re.sub(r"0x[0-9a-f]{2}",(chr(int(r"{\g<0>}",16))),istring)
    for strMatch in re.findall(r"0x[0-9a-f]{2}",istring):
        chrMatch = chr(int(strMatch,16))
        istring = re.sub(strMatch,chrMatch,istring)
    return istring

def make_flag(lists):
    flag = ""
    for each in lists[:-2]:
        flag += each[0]
        flag += each[-1]
        print(flag)
    for each in lists[-2:]:
        flag += each[0]
    return flag

def main():
    hexInput = get_inputs()
    bigList = hex_to_chrs(hexInput)
    lists = eval(bigList)
    print(make_flag(lists))

main()
