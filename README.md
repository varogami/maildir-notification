DESCRIPTION
Lightweight bash script that notify new mail from multiple maildir on desktop GUI with notify, on shell, on remote with jabber instant messaging or show on conky  system monitor ( http://conky.sourceforge.net/ )

INSTALL

First open maildir-notification file and put your maildirs path on MAILDIRS array.
Second make a dir where script will write files and put the path on TMPPATH.
Check that /usr/share/icons/gnome/48x48/actions/mail_new.png exist, with no install gnome-icon* package.
Correct XMPPNOTIFY and MIMEDECODER with full path of the script like:

XMPPNOTIFY='python /home/user/scripts/xmpp-notify.py'
MIMEDECODER='/home/user/scripts/mimedecode.pl'

Put username and password and user to destination of jabber notification (you need of two accounts)
If you want change other config (LIMIT_SUB, TIME etc, etc)

HOT TO USE

maildir-notification loop		notify every TIME with libnotify
maildir-notification loop std		notify on standard output
maildir-notification loop xmpp		notify to your jabber account

summary		     	  		show a summary of new mail with libnotify
summary std				show a summary on standard outpunt
summary-conky 				print a summary readable by conky (you must to put "text_buffer_size 512" in cokyrc)

reset					clean files and all recorded notification

count 					return total number of new mail (to use with some windows manager like awesome)

