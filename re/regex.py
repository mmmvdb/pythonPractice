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