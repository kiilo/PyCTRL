#Serialclass

import threading
import LOG
import time
import sys


class SerRecv(threading.Thread):
    def __init__(self, SerDev, queue, SeperatorStr):
        threading.Thread.__init__(self)
        self.SerDev = SerDev
        self.setDaemon(True)
        self.running = True
        self.buf = ''
        self.queue = queue
        self.SeperatorStr = SeperatorStr
        
    def readto(self, maxsize=None, timeout=0):
        """maxsize is ignored, timeout in seconds is the max time that is waiting for a complete line"""
        tries = 0
        while self.running:
            try:
                self.buf += self.SerDev.read(128)
            except OSError:
                self.running = False
                CaughtInTheAct(self.SerDev)
            pos = self.buf.find(self.SeperatorStr)
            if pos >= 0:
                line, self.buf = self.buf[:pos+1], self.buf[pos+1:]
                return line
            tries += 1
            if tries * self.SerDev.timeout > timeout:
                break
        line, self.buf = self.buf, ''
        return line
    
    def run(self):
        while self.running:
            s = self.readto()
            print(s+'\r')
#            s = self.SerDev.read(128)
 #           self.queue.put(s)
#            if s != '':
#                MAINlogger.debug(self.SerDev.portstr + dump(s))
            time.sleep(0.01)
            
    def stop(self):
        self.running = False
        self.SerDev.close

def CaughtInTheAct(SerDev):
    LOG.MAIN.error('CAUGHT IN THE ACT! serial device unplugged?' + SerDev.portstr)
    time.sleep(0.5)
    LOG.MAIN.debug("STOP all activity for now, until I find a solution to turn over lost interfaces ...")
    sys.exit()
    