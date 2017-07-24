# clipPhoneEmailExtractor

# This is the project for the end of the regular expressions chapter of "Automate the Boring Stuff with Python"
# We need to create a program that will read text in from the clipboard of the os, scan the text for any phone numbers or e-mail
# addresses and put only the numbers and addresses back into the clipboard.


import pyperclip
import re


# ***** Get text from the clipboard

clipboardText = str(pyperclip.paste())


# ***** Find all addresses and e-mails in given text

# We're just going to steal the phone number regex from earlier in the chapter:

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?             # area code, with or without parens, returned as a group and the whole thing optional
    (\s|-|\.)?                     # area code seporator as a space, -, or period, returned as a group and optional
    (\d{3})                        # number prefix
    (\s|-|\.)                      # prefix code seporator as a space, -, or period, returned as a group
    (\d{4})                        # number suffix
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension with zero or more spaces before, ext, x, or ext. space and 2-5 numbers returned group
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+           # username
    @                           # at
    [a-zA-Z0-9.-]+              # domain
    (\.[a-zA-Z]{2,4})           # dot something 2-4 chars (com, uk, edu stuff like that)
)''', re.VERBOSE)

# Let's find the matches

matches = []

for groups in phoneRegex.findall(clipboardText):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    
    matches.append(phoneNum)

for groups in emailRegex.findall(clipboardText):
    matches.append(groups[0])


# ***** Place numbers and addresses in the clipboard

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard.')
    print('\n'.join(matches))
else:
    print('No phone numbers or e-mail addresses found.')

