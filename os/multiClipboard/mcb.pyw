# So the first thing about this that is cool... apparently pyw means it won't show a terminal when running... but other than that
# it's a python script

# Multiclipboard
# The purpose of this is to create a program that will save the contents of the clipboard under different keywords so they 
# can be retreved later.  We'll use parameters to the script to save clipboard contents to a file, and later they can be retreived
# and placed back in the clipboard for us.  And we'll add an option to dump out the list of the file so we can remember what
# we've saved before.

# To use you can run from the run prompt in windows
# @pyw.exe c:\[path]\mcb.pyw %*

# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# ==== Save clipboard content ====
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # ==== List keywords and load content ====

    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))

    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    
mcbShelf.close()