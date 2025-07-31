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
        #breakpoints
        0xdeadbeafcafebabe
    """)
    return p


p = conn()


p.sendline(payload)

p.interactive() # Keep interaction open
