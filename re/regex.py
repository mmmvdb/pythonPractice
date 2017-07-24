import re

# You already know about regex, but here is the basics again in python


# re is the modual for regular expressions

# To set up the regex rule, you use re.compile, passing the expression and collecting the object
# Then to use it, you use the object's .search passing the text, returning a group object
# To access the group you can call group() or group(0).
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')

mo = phoneNumRegex.search('My number is 415-555-4242.')

print('Phone number found: ' + mo.group())
print('Phone number found: ' + mo.group(0))

# Parens in the regex rule set up more grouping options, which can be used later in your code
# in this case, we've seporated areacode and number.
phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')

mo = phoneNumRegex.search('My number is 415-555-4242.')

print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())

# There is also a groups() method that will return all groups

print(mo.groups())

# These groups are returned as tuples, so you can be all python about it

areaCode, mainNumber = mo.groups()

print("Area code:", areaCode)
print("Main number :", mainNumber)

# If you actually have to look for a paren in your expression, you can escape it with \

# There is a bunch of stuff I already know about regular expressions... I'm not going to write examples of them, but I'll 
# go ahead and note some stuff here

# | pipes can qualify like an if, so you could search for x | y, and you can excape a pipe \|

# ? question marks match optionally (zero or one).  So something like (wo)?man would match man and woman
# Again \? if you need to

# * asterisk matches 0 or more.
# Again \*

# + plus matches one or more.
# \+

# Repetitions can be specified by curley braces {#} like I did above with the phoneNumRex
# if you need a range, you can change the numbers in the braces something like this {3,5} which means 3 4 or 5.
# and you can do stuff like {,3} or {3,} which means 0 to 3 and 3 or more respectively

# But this is something new to me.

# The value returned in the group object is "greedy"
# That is it returns the largest string that qualified the expression

greedyHaRegex = re.compile(r'(Ha){3,5}')

mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

# But you can change that behavior by adding a ? at the end of the repetition statement like so:

greedyHaRegex = re.compile(r'(Ha){3,5}?')

mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

# I wonder if we still get all qualifcations in the group list... let's find out.

print(mo1.groups())

# Hmm, I wasn't expecting that, I don't really understand what happened there.  I suppose, it only returned the group part, and it
# was repeated to find the full string.  If that makes sense.  Basically the group was the small part that was repeated, and we gave
# rules for how many repeats we'd accept, but the group is still filled with the smaller part?  Dunno

# So now we learn maybe a bit more about that
# Find all returns a list of all matches

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')

mo = phoneNumRegex.findall('My number is 415-555-4242. Cell: 518-666-1542')

print(mo)

# And if you have groups, it returns tuples of matches

phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')

mo = phoneNumRegex.findall('My number is 415-555-4242. Cell: 518-666-1542')

print(mo)

# So that's nice, let's see what it does with our HaHaHaHaHa

mo1 = greedyHaRegex.findall('HaHaHaHaHa')

print(mo1)

# Weird, I guess it does the same thing... still dunno

# I used \d above for digits, here is a list of some more character classes
# \d    Numeric digits 0-9
# \D    Any non-numeric digit
# \w    "word", any letter, digit, or _
# \W    The opposite of above
# \s    Space, tab, newline
# \S    Opposite of that
# [0-5] Shorthand for 0, 1, 2, 3, 4, 5.  You can change this

xmasRegex = re.compile(r'\d+\s\w+')

mo = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')

print(mo)

# Actually that short hand is called creating your own character classes
# You can make your own by placing chars in brackets []
# These don't need escape chars.  And you can use dashes to go from one char to another
# I.E. [a-zA-Z0-9] for alphanumeric
# You can make it a negative class (any char not in the class qualifies) by having a ^ right after the opening brackets

punctRegex = re.compile(r'[!.?,;:\'"]')

mo = punctRegex.findall("'Is this some kind of test?', remarked Gandalf! ;.:\" \\")

print(mo)

# Some other things you've seen but not had to use...
# ^ sign can force the pattern match to the beginning of the string.
# $ to the end.  IE '^Hello', '\d$' or '^blahblah$'

# . can be wildcards matching any character but a newline. /. escapes it for a real period

atRegex = re.compile(r'.at')
mo = atRegex.findall('The cat in the hat sat on the flat mat.')

print(mo)

# .* matches all text, sometimes useful, and does it in a greedy way. .*? matches non greedy

nongreedyRegex = re.compile(r'<.*?>')
greedyRegex    = re.compile(r'<.*>')

mo = nongreedyRegex.search('<To serve man> for dinner.>')

print(mo.group())

mo = greedyRegex.search('<To serve man> for dinner.>')

print(mo.group())

# The . being all chars except newline can be changed by adding re.DOTALL as the second param to compile
# Now it will identify newlines too

# By defult as well, regex is case sensitive, but you can re.I or re.IGNORECASE to change that behavior

# Okay, now on to subsitutions.
# Using the sub() method, you can search a string, and replace the identified charaters.
# It takes two params obviously.

namesRegex = re.compile(r'Agent \w+')

mo = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')

print(mo)

namesRegex = re.compile(r'Agent (\w)\w*')

mo = namesRegex.sub(r'\1****', 'Agent Alice gave the secret documents to Agent Bob.')

print(mo)

# If your expressions get really large, you can pass an option to the compile, to allow for "verbose" expressions.
# These expressions allow whitespace and comments, so you can better document what the heck your doing in that blob of
# almost random characters.

# OMG no...
# phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

phoneRegex = re.compile(r'''
    (\d{3}|\(\d{3}\))?            # area code, with or without parens, returned as a group and the whole thing optional
    (\s|-|.)?                     # area code seporator as a space, -, or period, returned as a group and optional
    \d{3}                         # number prefix (why no group here?)
    (\s|-|.)                      # prefix code seporator as a space, -, or period, returned as a group
    \d{4}                         # number suffix (why no group here?)
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension with zero or more spaces before, ext, x, or ext. space and 2-5 numbers returned group
''', re.VERBOSE)

mo = phoneRegex.search('My number is 415-555-4242.')

print(mo.group())

# If you need multiple flags to pass to compile, you bitwise or them together with |
# I.E. someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)