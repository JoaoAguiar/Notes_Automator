#!/bin/python3.7

import sys
import os 

class NoteAutomator: 
    ruby = ".rb"
    php = ".php"
    javascript = ".js"
    typescript = ".ts"
    python = ".py"
    java = ".java"
    dart = ".dart"
    text = ".txt"
    xml = ".xml"
    html = ".html"
    css = ".css"
    json = ".json"
    c = ".c"
    cpp = ".cpp"
    csharp = ".cs"
    sql = ".sql"

    extensions = {
        "python" : python,
        ".python" : python,
        ".py" : python,
        "py" : python,
        "text" : text,
        ".text" : text,
        ".txt" : text,
        "txt" : text,
        "java" : java,
        ".java" : java,
        "php" : php,
        ".php" : php,
        "html" : html,
        ".html": html,
        "css" : css,
        ".css" : css,
        "javascript" : javascript,
        ".javascript" : javascript,
        "js" : javascript,
        ".js" : javascript,
        "ts" : typescript,
        ".ts" : typescript,
        "jason" : json,
        ".jason" : json,
        "json" : json,
        ".json" : json,
        "ruby" : ruby,
        ".ruby" : ruby,
        ".rb" : ruby,
        "rb" : ruby,
        "dart" : dart,
        ".dart" : dart,
        "xml" : xml,
        ".xml" : xml,
        "sql" : sql,
        ".sql" : sql,
        "c" : c,
        ".c" : c,
        "c++" : cpp,
        ".c++" : cpp,
        "c#" : csharp,
        ".c#" : csharp
    }

    extension          = ""
    folderName         = ""
    fileName           = ""
    path               = os.getcwd()

    def getArgs(self, ext, folder, name):
        try:
            self.extension = str(ext)
            self.extension = self.extensions[self.extension]
        except Exception:
            self.extension = ".txt"
        
        try:
            self.folderName = str(folder)
        except Exception:
            self.folderName = "General"
        
        try:
            self.fileName = str(name)
        except Exception:
            self.fileName = "general"

    def createNote(self):
        self.fileName = self.fileName + self.extension
        
        # Caso a pasta ja exista vai para ela
        # Caso a pasta nao exista cria uma com o nome folderName e vai para ela
        if os.path.isdir("./" + self.folderName):
            os.chdir("./" + self.folderName)
        else:
            os.mkdir(self.folderName)
            os.chdir("./" + self.folderName)
    
        # Caso o ficheiro ainda nao exista, ele cria
        if not os.path.isfile("./" + self.fileName):
            open(self.fileName, "a").close()

        # Abre a nota no Sublime
        os.system("notepad.exe " + self.fileName)

if __name__ == "__main__":
    notes = NoteAutomator()

    ext = ""
    folder = ""
    name = ""

    command = str(sys.argv[0])

    if command == "notes.py":
        try:
            opts = str(sys.argv[1])

            nOptions = len(opts)
            
            if(nOptions == 1):
                option1 = opts[0]

                if option1 == "e":
                    ext = str(sys.argv[2])
                    folder = "General"
                    name = "general"
                elif option1 == "f":
                    ext = ".txt"
                    folder = str(sys.argv[2])
                    name = "general"
                elif option1 == "n":
                    ext = ".txt"
                    folder = "General"
                    name = str(sys.argv[2])
                else:
                    print("Error! Options are kinda wrong")
            elif(nOptions == 2):
                option1 = opts[0]
                option2 = opts[1]

                if option1 == "e":
                    ext = str(sys.argv[2])

                    if option2 == "f":
                        folder = str(sys.argv[3])
                        name = "general"
                    elif option2 == "n":
                        folder = "General"
                        name = str(sys.argv[3])
                    else:
                        print("Error! Options are kinda wrong")  
                elif option1 == "f":
                    folder = str(sys.argv[2])

                    if option2 == "e":
                        ext = str(sys.argv[2])
                        name = "general"
                    elif option2 == "n":
                        ext = ".txt"
                        name = str(sys.argv[2])
                    else:
                        print("Error! Options are kinda wrong")  
                elif option1 == "n":
                    name = str(sys.argv[2])

                    if option2 == "e":
                        ext = str(sys.argv[3])
                        name = "general"
                    elif option2 == "f":
                        ext = ".txt"
                        folder = str(sys.argv[3])
                    else:
                        print("Error! Options are kinda wrong")  
                else:
                    print("Error! Options are kinda wrong")              
            elif(nOptions == 3):
                option1 = opts[0]
                option2 = opts[1]
                option3 = opts[2]

                if option1 == "e":
                    ext = str(sys.argv[2])

                    if option2 == "f":
                        folder = str(sys.argv[3])

                        if option3 == "n":
                            name = str(sys.argv[4])
                        else:
                            print("Error! Options are kinda wrong")  
                    elif option2 == "n":
                        name = str(sys.argv[3])

                        if option3 == "f":
                            folder = str(sys.argv[4])
                        else:
                            print("Error! Options are kinda wrong")                         
                    else:
                        print("Error! Options are kinda wrong")  
                elif option1 == "f":
                    folder = str(sys.argv[2])

                    if option2 == "e":
                        ext = str(sys.argv[3])

                        if option3 == "n":
                            name = str(sys.argv[4])
                        else:
                            print("Error! Options are kinda wrong") 
                    elif option2 == "n":
                        name = str(sys.argv[2])

                        if option3 == "e":
                            ext = str(sys.argv[4])
                        else:
                            print("Error! Options are kinda wrong") 
                    else:
                        print("Error! Options are kinda wrong")  
                elif option1 == "n":
                    name = str(sys.argv[2])

                    if option2 == "e":
                        ext = str(sys.argv[3])

                        if option3 == "f":
                            folder = str(sys.argv[4])
                        else:
                            print("Error! Options are kinda wrong")  
                    elif option2 == "f":
                        folder = str(sys.argv[3])

                        if option3 == "e":
                            ext = str(sys.argv[4])
                        else:
                            print("Error! Options are kinda wrong")  
                    else:
                        print("Error! Options are kinda wrong")  
                else:
                    print("Error! Options are kinda wrong")  
            else:
                print("Error! Options are kinda wrong")
        except Exception:
            print("Error! You didnt put the options")

        notes.getArgs(ext, folder, name)
        notes.createNote()
