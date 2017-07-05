#!/usr/bin/python2

# pacman -S xmpppy
# apt-get install python-xmpp

import sys, xmpp, time

# constants
wait=15 #15
TT=5

class Xnotify:
    def __init__(self, msg, bot_name, bot_pass, bot_server, user):
        self.msg = msg
        self.bot_name = bot_name
        self.bot_pass = bot_pass
        self.bot_server = bot_server
        self.user = user
        self.done = True
        self.debug = False

    def xmpp_send(self, JABBER_ID, JABBER_SERVER, JABBER_PASS, TO_JABBER_ID, MSG):
        jid=xmpp.protocol.JID(JABBER_ID)
        
        if self.debug:
            cl=xmpp.Client(jid.getDomain())
        else:
            cl=xmpp.Client(jid.getDomain(),debug=[])

#        while not cl.connect((JABBER_SERVER,5222)):
#            time.sleep(wait)
#            if not cl.connect((JABBER_SERVER,5222)):
#                raise IOError('Can not connect to server.')

#        while not cl.auth(jid.getNode(),JABBER_PASS,"LFY-client"):
#            time.sleep(wait)
#            if not cl.auth(jid.getNode(),JABBER_PASS,"LFY-client"):
#                raise IOError('Can not auth with server.')

        cl.connect((JABBER_SERVER,5222))
        cl.auth(jid.getNode(),JABBER_PASS,"LFY-client")
        cl.sendInitPresence()

        message = xmpp.Message( TO_JABBER_ID , MSG )
        message.setAttr('type', 'chat')
        cl.send( message )
        cl.disconnect()
        
    def do(self):
        if self.debug:
            self.xmpp_send( self.bot_name, self.bot_server, self.bot_pass, self.user, self.msg)
        else:
            try:
                self.xmpp_send( self.bot_name, self.bot_server, self.bot_pass, self.user, self.msg)
            except:
                self.done = False
                print "xmpp-notify.py: error send msg with - " + self.bot_name + " - trying " + str(TT) + " time again"
                print "xmpp-notify.py: msg - " + self.msg

            if not self.done:
                for num in range(0,TT):
                    if not self.done:
                        time.sleep(wait)
                        print "xmpp-notify.py: retry - " + str(num)
                        try:
                            self.xmpp_send( self.bot_name, self.bot_server, self.bot_pass, self.user, self.msg)
                            self.done = True
                        except:
                            self.done = False
                            print "xmpp-notify.py: error send msg with - " + self.bot_name
                            print "xmpp-notify.py: msg - " + self.msg
                    else:
                        break
                        
if __name__ == "__main__":
    notif = Xnotify(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    notif.do()
