#!python3
'''
Strong Password Protection
'''

import pyperclip, re

strongPwdRegex = re.compile(r'(A-Za-z)(0-9)+{8,}')

password = str(pyperclip())
matches = []

for groups in strongPwdRegex.findall(password):
    if len(matches) < 8:
        print('Password needs to be at least 8 characters.')