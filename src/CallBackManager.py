from OSC import * 

class CallbackManager:
    """This utility class maps OSC addresses to callables.
    The CallbackManager calls its callbacks with a list
    of decoded OSC arguments, including the address and
    the typetags as the first two arguments."""
    
    def __init__(self):
        self.callbacks = {}
        self.add(self.unbundler, "#bundle")

    def handle(self, data, source = None):
        """Given OSC data, tries to call the callback with the
        right address."""
        decoded = decodeOSC(data)
        self.dispatch(decoded)

    def dispatch(self, message):
        """Sends decoded OSC data to an appropriate calback"""
        try:
            address = message[0]
            self.callbacks[address](message)
        except KeyError, e:
            # address not found
            print 'foo'
            pass
        except None, e:
            print "Exception in", address, "callback :", e
        
        return

    def add(self, callback, name):
        """Adds a callback to our set of callbacks,
        or removes the callback with name if callback
        is None."""
        if callback == None:
            del self.callbacks[name]
        else:
            self.callbacks[name] = callback

    def unbundler(self, messages):
        """Dispatch the messages in a decoded bundle."""
        # first two elements are #bundle and the time tag, rest are messages.
        for message in messages[2:]:
            self.dispatch(message)

#manager = CallbackManager()