from irc_class import *
import os
import random

## IRC Config
server = "185.30.166.38"  # Provide a valid server IP/Hostname
port = 6697
channel = "#python"
botnick = "stwins60"
botnickpass = ""
botpass = "<%=  %>"
irc = IRC()
irc.connect(server, port, channel, botnick, botpass, botnickpass)

while True:
    text = irc.get_response()
    print(text)

    if "PRIVMSG" in text and channel in text and "hello" in text:
        irc.send(channel, "Hello!")