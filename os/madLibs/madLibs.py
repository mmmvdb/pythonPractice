# madLibs
# This is going to take in a file, scan it for all the all caps words "ADJECTIVE", "NOUN", "ADVERB", "VERB"
# then offer the user the ability to enter text to replace each one.  Then we'll print the results to screen
# and place the results in a file.

import re

# ==== Read in text file ====
madLibFile = open('madLib.txt')

madLibString = madLibFile.read()

print(madLibString)

# The ADVERB NOUN ADJECTIVE VERB the NOUN's VERB.

madLibSearch = re.compile(r'^(.*?)(ADJECTIVE|NOUN|ADVERB|VERB)(.*?)$')

search = madLibSearch.search(madLibString)

# ==== Loop over results where we find one of the keywords ====
while search != None:
    
    # prompt user for a replacement
    if search.group(2)[0] == 'A':
        replaceWord = input("Enter an " + search.group(2).lower() + ':')
    else:
        replaceWord = input("Enter a " + search.group(2).lower() + ':')
    
    # perform the replace
    
    madLibString = search.group(1) + replaceWord + search.group(3)
    
    search = madLibSearch.search(madLibString)
    
# Take the string and append it to the result file and print the result

resultFile = open('madLibResult.txt', 'a')

resultFile.write(madLibString + '\n')

resultFile.close()

print(madLibString)