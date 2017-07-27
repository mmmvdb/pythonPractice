#folderRegex

# Takes a folder and regex expression supplied by argument to the script, and searches all txt files with that folder with the 
# regex, displaying any matches in the console

# folderRegex.py - Search a folder for all .txt files and search them with the regex
# Usage:   folderRegex.py <path> <regex expression>
# Example: folderRegex.py C:\Windows\Temp ^Hello

import sys, re, os

# ==== Gather arguments ====
if len(sys.argv) == 3:
    path     = sys.argv[1]
    reString = sys.argv[2]

    print(reString)
    reSearch = re.compile(reString)
    
    # ==== Navigate to the folder ====
    if os.path.isdir(path):
        os.chdir(path)
    else:
        print(path + ' is an invalid path')
    
    # ==== Gather all txt files ====
    for filename in os.listdir('.'):
        if filename.endswith('.txt'):
            # ==== In each file, use the regex to find a match ====
            file = open(os.path.join(os.getcwd(),filename))
            fileLineList = file.readlines()
            file.close()
            
            for line in fileLineList:
                reResult = reSearch.search(line)
            
                if reResult != None:
                    #    ==== Print the result ====
                    print(filename + ': ' + line)

else:
    print('folderRegex.py - Search a folder for all .txt files and search them with the regex')
    print('   Usage:   folderRegex.py <path> <regex expression>')
    print('   Example: folderRegex.py C:\Windows\System32 ^Hello')

