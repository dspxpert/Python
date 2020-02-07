#
# DTMF_Gen.py
#
# Generate "dtmf_tone.h" file
# each DTMF single tone has 50ms of 8KHz sampling(400 samples)
# with amplitude of 80% of 7bit resolution
#
# Made by Jin-Deog Kang, HUMAX Networks HW Team.
# 

import math

freq = [697, 770, 852, 941, 1209, 1336, 1477, 1633]
ampl = 0.8
twopidt = 2 * math.pi / 8000

fname='dtmf_tone.h'
f = open(fname, 'w')
f.write('const int8_t dtmf_tone[8][400] PROGMEM = {\n') 

for num in range(8):
  f1_2pidt = twopidt * freq[num];
  f.write('{')  
  for i in range(400):
    dac = int(64 * ampl * math.sin(f1_2pidt*i))
    f.write(str(dac))
    if i < 399:
      f.write(', ')

  f.write('}')
  if num < 7:
    f.write(',\n')
  else:
    f.write('\n')

f.write('};\n')
f.close()
