--- 
customlog: 
  - 
    format: combined
    target: /etc/apache2/logs/domlogs/highscore.a2hosted.com
  - 
    format: "\"%{%s}t %I .\\n%{%s}t %O .\""
    target: /etc/apache2/logs/domlogs/highscore.a2hosted.com-bytes_log
documentroot: /home/highscor/public_html
group: highscor
hascgi: 0
homedir: /home/highscor
ifmodulemodsuphpc: 
  group: highscor
ifmodulemoduserdirc: {}

ip: 75.98.175.71
owner: root
phpopenbasedirprotect: 1
port: 80
scriptalias: 
  - 
    path: /home/highscor/public_html/cgi-bin
    url: /cgi-bin/
secruleengineoff: 1
serveradmin: webmaster@highscore.a2hosted.com
serveralias: mail.highscore.a2hosted.com www.highscore.a2hosted.com
servername: highscore.a2hosted.com
ssl: 1
usecanonicalname: 'Off'
user: highscor
userdirprotect: ''
