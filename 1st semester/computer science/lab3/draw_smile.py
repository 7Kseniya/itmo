eyes_gen = {0: ';', 1: ':', 2: 'X', 3: '8', 4: '='}
noses_gen = {0: '-', 1: '<', 2: '-{', 3: '<{'}
mouths_gen = {0: '(', 1: ')', 2: 'O', 3: '|', 4: '\\', 5: '/', 6: 'P'}

isu = int(input('your isu:'))
eyes = eyes_gen.get(isu % 5)
nose = noses_gen.get(isu % 4)
mouth = mouths_gen.get(isu % 7) 

print("your smile: %s " % (eyes + nose + mouth))
