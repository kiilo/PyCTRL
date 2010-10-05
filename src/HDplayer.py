

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
        SendToHDplayer( Address, Level)

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

HDplayerdev = '/dev/ttyUSB4'
# HDplayer serial setupt 
HDplayerser = serial.Serial(HDplayerdev, 38400, timeout=0.2, rtscts=0, xonxoff=0)


# serial.Serial(BEAMER01dev, 9600, timeout=0.02, 
#                    rtscts=1, 
#                    xonxoff=0)


def HDplayerPlayFile(message):
    LOG.OSC.debug('HDplayer '+ str(message[1:]))
    if message[1] == ',s':
        file = message[2]
        HDplayerser.write('(' + file + ')\r')
        #HDplayerser.write('\r')
    # GO TO SCENE Command 16 - 31 YAAA AAA1 0001 XXXX 




    

#########################################################################