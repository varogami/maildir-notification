#!/usr/bin/env python

import sys, pynotify, subprocess, gobject, gtk

#from gi.repository import Notify
#from gi.repository import GObject

class MyNotify:
    def __init__(self, icon, title, body, dir, id):
        self.icon = icon
        self.title = title
        self.body = body
        self.dir = dir
        self.id = id
        pynotify.init('Mail')
        self.main()

    def main(self):
        n = pynotify.Notification(self.title, self.body)
        n.add_action("action", "Open", self.action_callback)        
        n.show()
#        gobject.timeout_add(10000, self.main)
        gtk.main()

    def action_callback(self, n, action):
        CMD="/usr/bin/mutt -R -f " + self.dir + " -e \"push l~i"+self.id+"\\n\\n\""
        subprocess.Popen(['sakura','-e',CMD])
#        gtk.main_quit()


#class MyClass(GObject.Object):
#    def __init__(self):
#        super(MyClass, self).__init__()
#        # lets initialise with the application name
#        Notify.init("myapp_name")

#    def send_notification(self, title, text, full_path_to_icon=""):
#        n = Notify.Notification.new(title, text, file_path_to_icon)
#        n.show()


if __name__ == "__main__":
    notif = MyNotify(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
#    my = MyClass()
#    my.send_notification("this is a title", "this is some text")        
