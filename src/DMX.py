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
        SendToDMX( Address, Level)

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

DMXdev = '/dev/ttyUSB1'
# DMX serial setupt 
DMXser = serial.Serial(DMXdev, 115200, timeout=0.1, rtscts=0, xonxoff=0)


def DMXFadeTime(FadeTime, FadeRate):
    '''
    This function sets a global fadetime and faderate
    TODO 
    * insert command docu 
    * insert timing table
    '''
def SendToDMX(Address, Level):
    DMXser.write('S' + str(Address) + 'V' + str(Level) + '\r')
    
def DMXSetLevel(message):
    LOG.OSC.debug('SetLevel '+ str(message[1:]))
    if message[1] == ',ii':
        Address = message[2]
        Level = message[3]
        DMXser.write('S' + str(Address) + 'V' + str(Level) + '\r')
    # GO TO SCENE Command 16 - 31 YAAA AAA1 0001 XXXX 


def DMXSetRGB(message):
    LOG.OSC.debug('SetLevel '+ str(message[1:]))
    if message[1] == ',iiii':
        Address = message[2]
        R = message[3]
        G = message[4]
        B = message[5]
        DMXser.write('S' + str(Address) + 'V' + str(R) + ',' + str(G) + ',' + str(B) + '\r')
    # GO TO SCENE Command 16 - 31 YAAA AAA1 0001 XXXX 

    

#########################################################################