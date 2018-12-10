import os
import json
import re  # Regular Expressions (https://docs.python.org/3.7/library/re.html)
import subprocess  # Used for calling/invoking CMD processes

from dbTools import Tools

class claspTools:
        # def __init__(self):
        #     self.test = 1

        class dirTools:
                def __init__(self):
                        with open("config.json") as f: # Gets directory from config.JSON to determine starting point
                                self.workPath = os.path.dirname(json.load(f)["directory"]+"\\projects\\")
                
                def createFolder(self, name):
                        """
                        Create a folder in the projects directory with the following name.

                        :param name: {string} - Name of folder to be created
                        """
                        if not isinstance(name, str):
                                raise ValueError("crateFolder(): String not entered for input.")

                        os.chdir(self.workPath)
                        newDir = "./" + name + "/"
                        if not os.path.exists(newDir):
                                os.makedirs(newDir)    
                                print("Created new project folder" + newDir)

claspTools.dirTools().createFolder('')

# def getList():
#     cmdOut = subprocess.check_output("clasp list", shell=True).decode("UTF-8") # Fetches raw console output of 'clasp list'

#     initRe = re.findall(r"1G(\w.[\s\S]*)", cmdOut)[0]# Filters out unwanted characters so only script name and URLs are found
#     scriptInfoRe = re.finditer(r"(.*?)\s{2}.*\s.*d/(.*)/", initRe) # Seperates name and script ID into a group

#     for i in scriptInfoRe:
#         print(i.group(1)+" | "+i.group(2))
