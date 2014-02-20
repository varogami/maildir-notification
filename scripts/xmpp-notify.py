#!/usr/bin/env python
#Copyleft 2013  varogami <varogami@autistici.org>

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys,xmpp

# constants
JABBER_ID = "yourusername@yourjabber.org"
JABBER_PASS = "yourpassword"
JABBER_SERVER = "yourjabber.org"
TO_JABBER_ID = "user-destination@yourjabber.org"
MSG = sys.argv[1]

jid=xmpp.protocol.JID(JABBER_ID)
cl=xmpp.Client(jid.getDomain(),debug=[])
if not cl.connect((JABBER_SERVER,5222)):
    raise IOError('Can not connect to server.')
if not cl.auth(jid.getNode(),JABBER_PASS):
    raise IOError('Can not auth with server.')

cl.send( xmpp.Message( TO_JABBER_ID , MSG ) )
cl.disconnect()


