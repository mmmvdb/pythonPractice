# Again you know most of the stuff around working with an OS and reading and writing files
# So I'm going to be light on the notes and stuff that I already know.

# You know about the slash difference in file paths between windows and unix.
# Actually OS X also uses forward slash like unix/linux.

# But since you will likely be writing utilities and such that might need to run
# in multiple operating systems, the os module provides the slash you should use based
# on where your program is running

import os

print(os.path.join('test','mike','secretfiles'))

# You can do cool python tricks with this, standard stuff

myFiles = ['accounts.txt','details.csv','invite.docx']

for filename in myFiles:
    print(os.path.join('c:\\Users\\MMM',filename))

# pretty standard stuff

# You can get the current working directory like this

print(os.getcwd())

# And you can change directory like this

os.chdir('..')

print(os.getcwd())

# Going back to the project folder
os.chdir('os')

# But you'll error if you don't catch the exception and the directory doesn't exist.

# For our next trick, you can create dirs like this
#os.makedirs(os.path.join(os.getcwd() , 'testmkdir'))

# This apparently errors if the directory already exists...
# You could fix that by doing something like:
dirPath = os.path.join(os.getcwd() , 'testmkdir')

if os.path.isdir(dirPath) == False:
    os.makedirs(dirPath)
    
# Supposedly that could race condition and you're supposed to use soemthing else, but I'm just learning so...

# Working with absolute and relative paths
# It should be pretty easy to switch from absolute and relative pathing in python

print(os.path.abspath('..\\..\\'))
print(os.path.isabs('..\\..\\'))
print(os.path.relpath('c:\\', os.getcwd()))

# There are some helper functions to get the "base name" or file name and the dir name
# from a given path.

print(os.path.basename('C:\\Windows\\System32\\calc.exe'))
print(os.path.dirname('C:\\Windows\\System32\\calc.exe'))

# And if you need both in a tuple you can use os.path.split

print(os.path.split('C:\\Windows\\System32\\calc.exe'))

# If you needed access to all the folders in a path, you could string split on os.sep

print('C:\\Windows\\System32\\calc.exe'.split(os.sep))

# On Unix, there is a blank at the beginning of lists like this (for root)

# On to more stuff...

# os.path.getsize(path) gives a size in bytes of a file in the path
# os.listdir(path) lists all the file names in the directory in the path

print(os.path.getsize('files.py'))
print(os.listdir('.'))

# let's get fun
totalSize = 0
dir = 'c:\\Windows\\System32'
for filename in os.listdir(dir):
    totalSize += os.path.getsize(os.path.join(dir, filename))
    
print(totalSize)

# So above I did some work researching how to make sure things exist since it seems things crash and burn if 
# they are not valid.  But now ATBSWP now goes into that a bit more

print(os.path.exists('c:\\Windows\\System32'))
print(os.path.exists('c:\\Windows\\System32\\calc.exe'))

print(os.path.isfile('c:\\Windows\\System32\\calc.exe'))
print(os.path.isfile('c:\\Windows\\System32'))

print(os.path.isdir('c:\\Windows\\System32'))
print(os.path.isdir('c:\\Windows\\System32\\calc.exe'))

# And on to file IO.  I know most of this stuff too from working with other languages, so I might be light on notes and examples

# open takes a second param as read write mode
helloFile = open(os.path.join(os.getcwd(), 'hello.txt'))

helloContent = helloFile.read()

print(helloContent)

helloFile.close()

# FILE.read() returns the whole file
# if you want to just return lines you can do a FILE.readlines().  This returns a list with linebreaks

sonnetFile = open('sonnet29.txt')

print(sonnetFile.readlines())

sonnetFile.close()

# He doesn't talk about it here, but it looks like there is a FILE.readline() as well, I bet you can iterate using that if you want.

# Writing, there are modes w and a for write and append plaintext

baconFile = open('bacon.txt', 'w')
baconFile.write('Hello world!\n')
baconFile.close()

baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()

print(content)

# This is new to me however.  There is an apparently standard module in python called shelve.  It can be used to save off variables
# and data for you.  You can use it like a save and open to the program and such.

import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie','Pooka','Simon']
shelfFile['cats'] = cats
shelfFile.close()

# To load this data in later you can do

shelfFile = shelve.open('mydata')
print(type(shelfFile))
print(shelfFile['cats'])
shelfFile.close()

# Now basically you can interact with the shelf object like it was a dictionary... so you can use things like keys and values
# He says that the values returned are 'list-like' and you'd need to list them, like below... I'm a bit unsure what exactly he means 
# there though, although keys does seem to need it, so maybe he is right.
shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()

# Now we are moving on to pprint... which I know nothing about except it probaby stands for pretty print.

import pprint

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]

print(pprint.pformat(cats))
print(cats)

fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()

# So the cool thing about the above he did is that pprint basically printed a syntatically correct list, that he saved in a py
# file so it could be imported into a python script, and the variable would be reset.

import myCats
print(myCats.cats)

# Q:1. What is a relative path relative to?

# A relative path is basically a way to navigate through the tree without going back to the root
  
# Q:2. What does an absolute path start with?

# usually a ./ which mean the current working directory
  
# Q:3. What do the os.getcwd() and os.chdir() functions do?

# gets the current working directory, and changes directory
  
# Q:4. What are the . and .. folders?

# They are not really folders, but aliases for the current working directory and the parent directory
  
# Q:5. In C:\bacon\eggs\spam.txt, which part is the dir name, and which part is the base name?

# the dir name is c:\bacon\eggs\ and the "base" or file is spam.txt
  
# Q:6. What are the three “mode” arguments that can be passed to the open() function?

# I'm sure there are more than just three, but "r" is read, "w" is write, and "a" is append
  
# Q:7. What happens if an existing file is opened in write mode?

# Writing will overwrite anything there
  
# Q:8. What is the difference between the read() and readlines() methods?

# read treats the whole file like a huge string, with new lines involved.  readlines breaks the lines into a list, still with the 
# newlines
  
# Q:9. What data structure does a shelf value resemble?
# a dictionary
