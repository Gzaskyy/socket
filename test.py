
a = 0x497E



b

d = c.to_bytes(2, 'big')

e = int((bin(d[0])[2:].zfill(8) + bin(d[1])[2:].zfill(8)), 2)

print('d=   ', d)

print('e = ==== ', e)

print('hdjasdasd : ', int('0100100101111110', 2))


if d == a[0]:
    print('haha')
else:
    print('no')

print(a)
print(b)
print(c)
