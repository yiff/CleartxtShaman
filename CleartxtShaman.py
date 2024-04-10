import os
import sys

word = ""
filepath2search = r''
foundFiles = []
multiInstanceSearch = False
caseInsensitiveSearch = False
fileType = ""

# def main code to be ran on loop
def main():
    global foundFiles
    global filepath2search
    global word
    global multiInstanceSearch
    global fileType
    
    if os.name == 'nt':
        os.system(r"title CleartxtShaman v1.0")
    else:
        sys.stdout.write("\x1b]2;CleartxtShaman v1.0\x07")
    
    print("[-----------------------]")
    print("   CleartxtShaman v1.0")
    print("[-----------------------]")
    
    validDirectoryCheck = False;
    while validDirectoryCheck == False:
        filepath2search = input(r'Path to search (example: C:\user\Desktop\recoveredFiles): ')
        if os.path.exists(filepath2search):
            validDirectoryCheck = True
        else:
            print("\'"+filepath2search+"\' doesn't appear to be a valid directory! Try again!\n")
    
    fileType = input(r'What file type would you like to search through? (example: .txt): ')
    word = input(r'Phrase to search for (example: @gmail.com): ')
    multiInstanceSearch = input("Would you like the search to stop at the first instance of your phrase? (Y/n): ").lower() == 'n'
    caseInsensitiveSearch = input("Would you like to perform a potentially less accurate case in-sensitive search? (y/N): ").lower() == 'y'

    print("\nSTARTING SEARCH FOR ALL FILES IN PROVIDED DIRECTORY CONTAINING PHRASE: \'"+word+"\'")
    filesChecked = 0
    for root, dirs, files in os.walk(filepath2search):
        for file in files:
            filesChecked+=1
            if os.name == 'nt':
                os.system(r"title CleartxtShaman v1.0 - Files Checked: "+str(filesChecked))
            else:
                sys.stdout.write("\x1b]2;CleartxtShaman v1.0 - Files Checked: "+str(filesChecked)+"\x07")
                
            if file.endswith(fileType):
                filepath = os.path.join(root, file)
                print("checking "+filepath)
                with open(filepath) as openFile:
                    try:
                        data = openFile.readlines()
                        
                        for line in data:
                            if(caseInsensitiveSearch == True):
                                if word.lower() in line.lower():
                                    foundFiles.append(filepath)

                            if word in line:
                                foundFiles.append(filepath)

                        openFile.close()
                        
                    except Exception:
                        pass
             
        if(len(foundFiles) != 0 and multiInstanceSearch == False):
            raise KeyboardInterrupt
    else:
        print("\nFINISHED! ALL FILES CHECKED FOR PHRASE: \'"+word+"\'")
        if(len(foundFiles) != 0):
            print("We found files that contain \'"+word+"\'! Here they are:")
            for i in foundFiles:
                print("\n[!] "+i)
            print("\n\n")
            foundFiles = []
            print("Press ENTER to try again!")
            input()
        else:
            print("We didn't find any files that contain \'"+word+"\' :(")
            print("\n\n")
            foundFiles = []
            print("Press ENTER to try again!")
            input()

# main app loop
if __name__ == '__main__':
    while True:
        try:
            main()
            
        except KeyboardInterrupt:
            print("\nSCAN STOPPED! FILES WERE CHECKED FOR PHRASE: \'"+word+"\'")
            if(len(foundFiles) != 0):
                print("We found files that contain \'"+word+"\'! Here they are:")
                for i in foundFiles:
                    print("\n[!] "+i)
                print("\n\n")
                foundFiles = []
                print("Press ENTER to try again!")
                input()
            else:
                print("We didn't find any files that contain \'"+word+"\' :(")
                print("\n\n")
                foundFiles = []
                print("Press ENTER to try again!")
                input()