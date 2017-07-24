import re

# You already know about regex, but here is the basics again in python


# re is the modual for regular expressions

# To set up the regex rule, you use re.compile, passing the expression and collecting the object
# Then to use it, you use the object's .search passing the text, returning a match object
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

# The value returned in the match object is "greedy"
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



# End questions

# Q:1. What is the function that creates Regex objects?

#    re.compile()
    
# Q:2. Why are raw strings often used when creating Regex objects?

#   Because you'd have to escape a bunch of frequently used characters like / if you didn't use raw.  Raw lets you avoid all that.

# Q:3. What does the search() method return?

#   I believe it returns a match object.

# Q:4. How do you get the actual strings that match the pattern from a Match object?

#   either by calling .group() or .group(0) on the object. 

# Q:5. In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group 0 cover? Group 1? Group 2?

#   all of the match, the areacode like thing, the number.

# Q:6. Parentheses and periods have specific meanings in regular expression syntax. How would you specify that you want a regex to match actual parentheses and period characters?

#   You'd have to escape them with a /

# Q:7. The findall() method returns a list of strings or a list of tuples of strings. What makes it return one or the other?

#   If you have groups it returns tuples

# Q:8. What does the | character signify in regular expressions?

#   It's an or, like match this or that.

# Q:9. What two things does the ? character signify in regular expressions?

#   It can mean to match 0 or 1 times, but depending on location can also make things non-greedy
    
# Q:10. What is the difference between the + and * characters in regular expressions?

#   * 0-any, + 1-any repetitions

# Q:11. What is the difference between {3} and {3,5} in regular expressions?

#   {3} three repetitions, {3,5} 3, 4, or 5 repetitions

# Q:12. What do the \d, \w, and \s shorthand character classes signify in regular expressions?

#   d = digit, w = letter, digit, or _, \s any space tab or newline

# Q:13. What do the \D, \W, and \S shorthand character classes signify in regular expressions?

#   they are just negetive classes of the above.  Any char but the ones above.

# Q:14. How do you make a regular expression case-insensitive?

#   At compile() time, you have to pass a re.IGNORECASE or re.I as a second param

# Q:15. What does the . character normally match? What does it match if re.DOTALL is passed as the second argument to re.compile()?

#   It normally means a any char but newline, but re.DOTALL can make it qualify any char even newlines 

# Q:16. What is the difference between these two: .* and .*?

#   .* qualifies any character sequence, and will qualify the most possible.  .*? Will qualify the least possible.

# Q:17. What is the character class syntax to match all numbers and lowercase letters?

#   [a-z0-9] is what I'd use

# Q:18. If numRegex = re.compile(r'\d+'), what will numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') return?

#   I'll test but I think it would return, "X drummers, X pipers, five rings, X hens", yep

# Q:19. What does passing re.VERBOSE as the second argument to re.compile() allow you to do?

#   It allows for whitespace and comments in the regex to make it easier to understand the big nasty stuff

# Q:20. How would you write a regex that matches a number with commas for every three digits? It must match the following:
#   '42'
#   '1,234'
#   '6,368,745'
# but not the following:
#   '12,34,567' (which has only two digits between the commas)
#   '1234' (which lacks commas)

#   Hmm, let's try

#niceNum = re.compile(r'\d{1,3}(,\d{3})+|\d{1,3}[^,\d]')
# This had some problems.

#   Let's try:

niceNum = re.compile(r'^\d{1,3}(,\d{3})*$')

print(niceNum.search('42'))
print(niceNum.search('1,234'))
print(niceNum.search('6,368,745'))
print(niceNum.search('12,34,567'))
print(niceNum.search('1234'))

# sort of cheating I guess if we wanted to find it in the middle of another string.  But I guess I could space it instead of
# end string it

# Q:21. How would you write a regex that matches the full name of someone whose last name is Nakamoto? You can assume that the 
#       first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:
#   'Satoshi Nakamoto'
#   'Alice Nakamoto'
#   'Robocop Nakamoto'
# but not the following:
#   'satoshi Nakamoto' (where the first name is not capitalized)
#   'Mr. Nakamoto' (where the preceding word has a nonletter character)
#   'Nakamoto' (which has no first name)
#   'Satoshi nakamoto' (where Nakamoto is not capitalized)

#   Let's try:

fullName = re.compile(r'[A-Z][a-z]+\sNakamoto')

print(fullName.search('Satoshi Nakamoto'))
print(fullName.search('Alice Nakamoto'))
print(fullName.search('Robocop Nakamoto'))
print(fullName.search('satoshi Nakamoto'))
print(fullName.search('Mr. Nakamoto'))
print(fullName.search('Nakamoto'))
print(fullName.search('Satoshi nakamoto'))

# Q:22. How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, 
#       or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive. It must match the following:
#   'Alice eats apples.'
#   'Bob pets cats.'
#   'Carol throws baseballs.'
#   'Alice throws Apples.'
#   'BOB EATS CATS.'
# but not the following:
#   'Robocop eats apples.'
#   'ALICE THROWS FOOTBALLS.'
#   'Carol eats 7 cats.'

#   Let's try:

sentenceRe = re.compile(r'(Alice|Bob|Carol) (eats|pets|throws) (apples|cats|baseballs)\s*.*\.', re.I)

print(sentenceRe.search('Alice eats apples.'))
print(sentenceRe.search('Bob pets cats.'))
print(sentenceRe.search('Carol throws baseballs.'))
print(sentenceRe.search('Alice throws Apples.'))
print(sentenceRe.search('BOB EATS CATS.'))
print(sentenceRe.search('Robocop eats apples.'))
print(sentenceRe.search('ALICE THROWS FOOTBALLS.'))
print(sentenceRe.search('Carol eats 7 cats.'))


#Practice Projects
#Strong Password Detection
#   Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong password is 
#   defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one 
#   digit. You may need to test the string against multiple regex patterns to validate its strength.

def strongPassword(password):
    #Lets do this the dumb way and just check for each
    
    capitols = re.compile(r'[A-Z]')
    lower    = re.compile(r'[a-z]')
    number  = re.compile(r'\d')
    length   = re.compile(r'.{8,}')
    
    if capitols.search(password) != None:
        capTest = capitols.search(password).group()
    else:
        capTest = ''
    if lower.search(password) != None:
        lowTest = lower.search(password).group()
    else:
        lowTest = ''
    if number.search(password) != None:
        numTest = number.search(password).group()
    else:
        numTest = ''
    if length.search(password) != None:
        lenTest = length.search(password).group()
    else:
        lenTest = ''
    
    print('capTest: ' + capTest)
    print('lowTest: ' + lowTest)
    print('numTest: ' + numTest)
    print('lenTest: ' + lenTest)
    
    if len(capTest) > 0 and len(lowTest) > 0 and len(numTest) > 0 and len(lenTest) > 0:
        return True
    else:
        return False

print(strongPassword('AndyLoves98'))
print(strongPassword('1lazypassword'))
print(strongPassword('5YELLING'))
print(strongPassword('ThisisaTest'))
print(strongPassword('Az9'))
        
        
#Regex Version of strip()
#   Write a function that takes a string and does the same thing as the strip() string method. If no other arguments are passed 
#   other than the string to strip, then whitespace characters will be removed from the beginning and end of the string. 
#   Otherwise, the characters specified in the second argument to the function will be removed from the string.

stripRe = re.compile(r'')