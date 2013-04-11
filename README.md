this readme can be outdated, see http://varogami.altervista.org/doku/maildir-notification for updated info

## DESCRIPTION

Lightweight bash script that notify new e-mail from multiple maildir (only e-mails in MAILDIR format) on desktop GUI with notify, on shell, on remote with jabber instant messaging or show on conky  system monitor ( http://conky.sourceforge.net/ )

## INSTALL

1. Need to python-xmpp, and perl.
2. open maildir-notification file and put your maildirs paths on `MAILDIRS` array.
3. make a dir where script will write files and put the path on `TMPPATH`.
4. Check that /usr/share/icons/gnome/48x48/actions/mail_new.png exist, if no install gnome-icon* package.
5. Correct `XMPPNOTIFY` and `MIMEDECODER` with full path of the script
6. Put username and password and user to destination of jabber notification in xmpp-notify.py
7. If you want change other config (LIMIT_SUB, TIME etc, etc)


## HOT TO USE

maildir-notification loop		           -> notify every TIME with libnotify   
maildir-notification loop std		       -> notify on standard output   
maildir-notification loop xmpp		     -> notify to your jabber account   
maildir-notification summary		     	 -> show a summary of new mail with libnotify   
maildir-notification summary std			 ->	show a summary on standard outpunt   
maildir-notification summary-conky 		 -> print a summary readable by conky    
                                        (you must to put "text_buffer_size 512" in cokyrc)   
maildir-notification reset				     -> clean files and all recorded notification   
maildir-notification count 				     -> return total number of new mail    
                                        (to use with some windows manager like awesome)   

