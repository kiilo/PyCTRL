"""
PyCTRL 

light control gateway OSC <-> Serial

Structure of sources
main.py - initialize & setup - main loop
OSC.py - OSC helping class defined here
Serial.py - helping classes defined here
Logging.py - logging to see what happens
"""

# imports
import sys
import os
import OSC
import CallBackManager
import time
import serial
import string
import Queue
import re
# my classes
import SerialClass
import LOG
import DALI
import DMX
import IRtrans
import HDplayer


#DALI.DALIdev = '/dev/ttyUSB0'
#DMX.DMXdev = "/dev/ttyUSB1"


# global callback (makes things easy)
MANAGER = CallBackManager.CallbackManager() # wired but true, please realize the small difference ;-)
MANAGER.add( OSC.Pong,'/ping')
MANAGER.add( DALI.SetLevel,'/RS/DALI/Licht')
MANAGER.add( DMX.DMXSetLevel, '/RS/DMX/Licht')
MANAGER.add( DMX.DMXSetRGB, '/RS/DMX/RGB')
MANAGER.add( IRtrans.IRtransPower, '/RS/IRtrans/power')
MANAGER.add( HDplayer.HDplayerPlayFile, '/RS/HDplayer')

# setup
def SetupMain():
    LOG.MAIN.debug('MAIN SETUP')
    OSC.SetupRecv('',9000, MANAGER)
    
# main loop)
def Main():
    LOG.MAIN.debug('MAIN LOOP')

SetupMain()
Main()
    
    