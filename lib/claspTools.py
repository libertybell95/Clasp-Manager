"""
Library for claspTools.

GAS = Google Apps Script
"""

import json
import os
import re
import subprocess
from lib.dbTools import dbTools as Tools

class claspTools:
        """Tools that call the Google Apps Script clasp service."""

        def __init__(self):
                """Init."""
                with open("config.json") as f: # Imports config.json file and assgns the object to self.config
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

                workPath = os.path.dirname( # Compiles directory string that represent projects folder
                        self.config["directory"]+"\\projects\\")

                # Changes working directory to projects folder
                os.chdir(workPath)
                newDir = "./" + name + "/"  # For use in os.makedirs

                if not os.path.exists(newDir):
                        """
                        If folder does not exist,
                        make new folder and perform setup
                        """
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

        def pushProject(self, name):
                """
                Pushes projcect/folder to GAS.

                :param name: {string} - Name of project/folder to be pushed
                """
                if not isinstance(name, str):
                        raise ValueError("pullFolder(): ")
                
                workPath = os.path.dirname(self.config["directory"]+"\\projects\\")
                os.chdir(workPath+"\\"+name)

                subprocess.check_output("clasp push", shell=True)  # Grabs files from Google Apps Script
