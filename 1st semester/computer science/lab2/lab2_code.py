msg, bits, count = input('message: '), [], 0

for i in msg:
    try: bits.append(int(i)) if count < 7 else ''
    except: bits.append(0)
    count += 1
s1 = bits[0] ^ bits[2] ^ bits[4] ^ bits[6]
s2 = bits[1] ^ bits[2] ^ bits[5] ^ bits[6]
s3 = bits[3] ^ bits[4] ^ bits[5] ^ bits[6]

print('syndrom: ', s1, s2, s3)

def ham(result = ''):
    for i in bits: result += str(i)
    return result

if (s1, s2, s3) == (0, 0, 0):
    print('no mistakes ', ham())
elif (s1, s2, s3) == (0, 0, 1):
    bits[3] = (bits[3] + 1) % 2
    print('mistake in r3', '.\nwrong bit = 4', '.\ncorrect massage: ', ham())
elif (s1, s2, s3) == (0, 1, 0):
    bits[1] = (bits[1] + 1) % 2
    print('mistake in r2', '.\nwrong bit = 2', '.\ncorrect massage: ', ham())
elif (s1, s2, s3) == (0, 1, 1):
    bits[5] = (bits[5] + 1) % 2
    print('mistake in i3', '.\nwrong bit = 6', '.\ncorrect massage: ', ham())
elif (s1, s2, s3) == (1, 0, 0):
    bits[0] = (bits[0] + 1) % 2
    print('mistake in r1', '.\nwrong bit = 1', '.\ncorrect massage: ', ham())
elif (s1, s2, s3) == (1, 0, 1):
    bits[4] = (bits[4] + 1) % 2
    print('mistake in i2', '.\nwrong bit = 5', '.\ncorrect massage: ', ham())
elif (s1, s2, s3) == (1, 1, 0):
    bits[2] = (bits[2] + 1) % 2
    print('mistake in i1', '.\nwrong bit = 3', '.\ncorrect massage: ', ham())
elif (s1, s2, s3) == (1, 1, 1):
    bits[6] = (bits[6] + 1) % 2
    print('mistake in i4', '.\nwrong bit = 7', '.\ncorrect massage: ', ham())