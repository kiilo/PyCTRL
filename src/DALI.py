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
        SendToDali( Address, Level)

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

DALIdev = '/dev/ttyUSB0'
# DALI serial setupt # 
DALIser = serial.Serial(DALIdev, 19200, timeout=0.1, rtscts=0, xonxoff=0)

def SendToDali( DaliHI, DaliLOW):
    '''
    send a command to dali - protocoll blows it up 
    TODO
    * document addressing scheme
    * insert basic command table
    '''

    XorCheck = 0
    dumpy = ''
    # StartCtrl
    DALIser.write( chr(0b00100000) )
    dumpy += chr(0b00100000) 
    XorCheck = 0b00100000
    
    # ADDR HI 
    DALIser.write( chr(0b00000000) )
    dumpy += chr(0b0000000) 
    XorCheck = XorCheck^( 0b00000000 )
    # ADDR MID
    DALIser.write( chr(0b00000000) )
    dumpy += chr(0b0000000)
    XorCheck = XorCheck^( 0b00000000 )
    # ADDR LOW
    DALIser.write( chr(0b00000000) )
    dumpy += chr(0b0000000)
    XorCheck = XorCheck^( 0b00000000 )
    
    # DATA HIGH
    DALIser.write( chr( DaliHI ) )
    dumpy += chr( DaliHI )
    XorCheck = XorCheck^( DaliHI )
    # DATA LOW
    DALIser.write( chr(DaliLOW ))
    dumpy += chr( DaliLOW )
    XorCheck = XorCheck^( DaliLOW )

    # XOR CHECK
    DALIser.write(chr(XorCheck))
    dumpy += chr( XorCheck )
    #print(dump( dumpy ))

def DaliFadeTime(FadeTime, FadeRate):
    '''
    This function sets a global fadetime and faderate
    TODO 
    * insert command docu 
    * insert timing table
    '''

    # set DTR to FadeTime
    SendToDali( 0b10100011, FadeTime)
    # STORE THE DTR AS FADE TIME
    # broadcast it to all
    SendToDali( 0b11111111, 0b00101110)

    # set DTR to FadeRate
    SendToDali( 0b10100011, FadeRate)
    # STORE THE DTR AS FADE RATE
    # broadcast it to all
    SendToDali( 0b11111111, 0b00101111)

def DaliGoToScene(DaliAddress, DaliScene):
    # GO TO SCENE Command 16 - 31 YAAA AAA1 0001 XXXX 
    SendToDali(DaliAddress, 0b00010000 | DaliScene)

#########################################################################