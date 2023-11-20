
import random
from string import ascii_uppercase
length = 5
kode =""
kodeList = [random.choice(ascii_uppercase) for _ in range(length)]
kodestr = ''.join(kodeList)

print(kodeList)
print(kodestr)