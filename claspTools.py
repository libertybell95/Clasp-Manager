import os
import json
import re  # Regular Expressions (https://docs.python.org/3.7/library/re.html)
import subprocess  # Used for calling/invoking CMD processes

from dbTools import Tools

class claspTools:
        def __init__(self):
            self.test = 1
                
        def createFolder(self, name, scriptID):
                """
                Create a new projects folder with nessecary setup files

                :param name: {string} - Name of folder to be created \n
                :param name: {string} - scriptID to create .clasp.JSON file
                """
                if not isinstance(name, str):
                        raise ValueError("createFolder(): String not entered for name.")
                elif not isinstance(scriptID, str):
                        raise ValueError("createFolder(): String not entered for scriptID.")
                
                with open("config.json") as f: # Gets directory from config.JSON to determine starting point
                        workPath = os.path.dirname(json.load(f)["directory"]+"\\projects\\")

                os.chdir(workPath)
                newDir = "./" + name + "/"
                if not os.path.exists(newDir):
                        os.makedirs(newDir)    
                        print("Created new project folder" + newDir)
                        os.chdir(newDir)

                with open(".clasp.json", "w") as f: # Sets up initial .clasp.json file
                        data = {
                                "scriptId": scriptID
                        }
                        json.dump(data, f, indent=4)

# def getList():
#     cmdOut = subprocess.check_output("clasp list", shell=True).decode("UTF-8") # Fetches raw console output of 'clasp list'

#     initRe = re.findall(r"1G(\w.[\s\S]*)", cmdOut)[0]# Filters out unwanted characters so only script name and URLs are found
#     scriptInfoRe = re.finditer(r"(.*?)\s{2}.*\s.*d/(.*)/", initRe) # Seperates name and script ID into a group

#     for i in scriptInfoRe:
#         print(i.group(1)+" | "+i.group(2))
