

#!/usr/bin/python
import serial
import string
import time
import LOG

def SetLevel(message):
    LOG.OSC.debug('SetLevel '+ str(message[1:]))
    if message[1] == ',ii':
        Address = message[2]
        Level = message[3] 
        SendToIRtrans( Address, Level)

#HEX dump
FILTER=''.join([(len(repr(chr(x)))==3) and chr(x) or '.' for x in range(256)])

def dump(src, length=24):
    N=0; result=''
    while src:
        s,src = src[:length],src[length:]
        hexa = ' '.join(["%02X"%ord(x) for x in s])
        s = s.translate(FILTER)
        result += "%04X   %-*s   %s\n" % (N, length*3, hexa, s)
        N+=length
    return result

IRtransdev = '/dev/ttyUSB2'
# IRtrans serial setupt 
IRtransser = serial.Serial(IRtransdev, 38400, timeout=0.2, rtscts=0, xonxoff=0)


# serial.Serial(BEAMER01dev, 9600, timeout=0.02, 
#                    rtscts=1, 
#                    xonxoff=0)

# '50 FA 06 00 FF FF 24 26 01 32 02 45 00 D2 00 1A 01 94 13 00 00 00 00 00 00 68 04 46 00 47 00 64 04 44 00 00 00 00 00 00 00 00 01 00 53 31 31 31 30 30 30 30 31 30 31 31 31 30 30 31 30 31 31 31 30 31 30 30 30 30 30 30 31 30 31 31 31 33 32 30' 



def IRtransPower(message):
    LOG.OSC.debug('IRtrans '+ str(message[1:]))
    pokes = [0x50, 0xFA, 0x06, 0x00, 0xFF, 0xFF, 0x24, 0x26, 0x01, 0x32, 0x02, 0x45, 0x00, 0xD2, 0x00, 0x1A, 0x01, 0x94, 0x13, 
             0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x68, 0x04, 0x46, 0x00, 0x47, 0x00, 0x64, 0x04, 0x44, 0x00, 0x00, 0x00, 0x00, 
             0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x53, 0x31, 0x31, 0x31, 0x30, 0x30, 0x30, 0x30, 0x31, 0x30, 0x31, 0x31, 0x31, 
             0x30, 0x30, 0x31, 0x30, 0x31, 0x31, 0x31, 0x30, 0x31, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x31, 0x30, 0x31, 0x31, 
             0x31, 0x33, 0x32, 0x30]
    if message[1] == ',s':
        power = message[2]
        for poke in pokes:
            IRtransser.write(chr(poke))
        #IRtransser.write('\r')
    # GO TO SCENE Command 16 - 31 YAAA AAA1 0001 XXXX 




    

#########################################################################