"""
Library for claspTools.

GAS = Google Apps Script
"""

import os
import json
import re # Regular Expressions (https://docs.python.org/3.7/library/re.html)
import subprocess # Used for calling/invoking CMD processes

from lib.dbTools import Tools


class claspTools:
        """Tools that call the Google Apps Script clasp service."""

        def __init__(self):
                """Init."""
                # Imports config.json file and
                # assigns the object to self.config
                with open("config.json") as f:
                        self.config = json.load(f)        
        
        def createProject(self, name, scriptID):
                """
                Create a new projects folder with nessecary setup files and pulls project from GAS.

                :param name: {string} - Name of folder to be created
                :param name: {string} - scriptID to create .clasp.JSON file
                """
                if not isinstance(name, str):
                        raise ValueError("String not entered for name.")
                elif not isinstance(scriptID, str):
                        raise ValueError("String not entered for scriptID.")

                # Compiles directory string that represents projects folder
                workPath = os.path.dirname(
                        self.config["directory"]+"\\projects\\")

                # Changes working directory to projects folder
                os.chdir(workPath)
                newDir = "./" + name + "/"  # For use in os.makedirs

                # If folder does not exist,
                # make new folder and perform setup
                if not os.path.exists(newDir):
                        os.makedirs(newDir)
                        print("Created new project folder" + newDir)

                        os.chdir(newDir)
                        

                        # Sets up initial .clasp.json file
                        with open(".clasp.json", "w") as f: 
                                data = {
                                        "scriptId": scriptID
                                }
                                json.dump(data, f, indent=4)

                        subprocess.check_output("clasp pull", shell=True) # Grabs files from Google Apps Script

        def pullProject(self, name):
                """
                Updates/Pulls project folder from GAS.

                :param name: {string} - Name of project folder to be updated
                """
                if not isinstance(name, str):
                        raise ValueError("pullFolder(): ")
                
                workPath = os.path.dirname(
                        self.config["directory"]+"\\projects\\"
                        )
                os.chdir(workPath+"\\"+name)

                subprocess.check_output("clasp pull", shell=True)  # Grabs files from Google Apps Script