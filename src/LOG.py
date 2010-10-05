# logging
import logging, logging.handlers

RemoteLogger = logging.getLogger('')
RemoteLogger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
    
LogFile = logging.FileHandler("MyModule.log")
LogFile.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s: %(name)-5s: %(levelname)-8s %(message)-s')
console.setFormatter(formatter)
LogFile.setFormatter(formatter)

logging.getLogger('').addHandler(console)
logging.getLogger('').addHandler(LogFile)

MAIN = logging.getLogger('MAIN')
OSC = logging.getLogger('OSC')

