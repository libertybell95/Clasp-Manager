import os
import json
import re  # Regular Expressions (https://docs.python.org/3.7/library/re.html)
import subprocess  # Used for calling/invoking CMD processes

from dbTools import Tools

class claspTools:
        def __init__(self):
            with open("config.json") as f: # Imports config.json file and assigns the object to self.config
                    self.config = json.load(f)
                
        def createProject(self, name, scriptID):
                """
                Create a new projects folder with nessecary setup files and pulls it from clasp

                :param name: {string} - Name of folder to be created \n
                :param name: {string} - scriptID to create .clasp.JSON file
                """
                if not isinstance(name, str):
                        raise ValueError("createFolder(): String not entered for name.")
                elif not isinstance(scriptID, str):
                        raise ValueError("createFolder(): String not entered for scriptID.")
                
                workPath = os.path.dirname(self.config["directory"]+"\\projects\\") # Compiles directory string that represents projects folder

                os.chdir(workPath) # Changes working directory to projects folder
                newDir = "./" + name + "/" # For use in os.makedirs
                
                if not os.path.exists(newDir): # If folder does not exist make new folder and perform setup
                        os.makedirs(newDir)    
                        print("Created new project folder" + newDir)
                
                        os.chdir(newDir)

                        with open(".clasp.json", "w") as f: # Sets up initial .clasp.json file
                                data = {
                                        "scriptId": scriptID
                                }
                                json.dump(data, f, indent=4)

                        subprocess.check_output("clasp pull", shell=True) # Grabs files from Google Apps Script

# def getList():
#     cmdOut = subprocess.check_output("clasp list", shell=True).decode("UTF-8") # Fetches raw console output of 'clasp list'

#     initRe = re.findall(r"1G(\w.[\s\S]*)", cmdOut)[0]# Filters out unwanted characters so only script name and URLs are found
#     scriptInfoRe = re.finditer(r"(.*?)\s{2}.*\s.*d/(.*)/", initRe) # Seperates name and script ID into a group

#     for i in scriptInfoRe:
#         print(i.group(1)+" | "+i.group(2))
