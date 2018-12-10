# Used to perform setup of JSON config file
import json
import os

os.chdir(os.path.dirname(os.path.realpath(__file__))) # Sets path to folder of file

data = {
    "directory": os.path.dirname(os.getcwd()), # Directory of program folder
    "dbName": "dbTools.py" # Name of central database
}

os.chdir("..")
with open("config.json", "w") as outfile:
    json.dump(data, outfile, indent=4)