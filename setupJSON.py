# Used to perform setup of JSON config file
import json
import os

data = {
    "directory": os.path.dirname(os.path.realpath(__file__)), # Directory of folder that this file is in
    "dbName": "dbTools.py" # Name of central database
}

with open("config.json", "w") as outfile:
    json.dump(data, outfile, indent=4)