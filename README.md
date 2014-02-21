DESCRIPTION
Lightweight bash script that notify new mail from multiple maildir on desktop GUI with notify, on shell, on remote with jabber instant messaging or show on conky  system monitor ( http://conky.sourceforge.net/ )

INSTALL
Clone git, copy whole maildir-notification directory on your favorite place.
Open maildir-notification file and set your maildirs path on MAILDIRS array and BASEDIR path with your "favorite place".
Launch maildir-notification reset

Put username and password and user to destination of jabber notification in xmpp-notify.py file (you need two accounts)
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

