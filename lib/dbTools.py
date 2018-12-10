"""Tools for modifying master Database."""

import sqlite3 # SqlLite (https://docs.python.org/3.7/library/sqlite3.html)

class Tools:
    """Tools for editing the Master database."""

    def __init__(self):
        """Tools init."""
        self.db = "gasMaster.db"
        self.conn = sqlite3.connect(self.db)
        self.cur = self.conn.cursor()

    def close(self):
        """Commit and close active DB connection."""
        self.conn.commit()
        self.conn.close()

    def projectsInsert(self, scriptID, pName, pDesc=''):
        """
        Insert values into projects table.
        
        :param scriptID: {string} - Script ID (Found in project GUI under: File - Project Properties - Info)
        :param pName: {string} - Project Name. Usually what it's called in Google Apps Script
        :param pDesc: {string} (Optional) - Project description. A short description of what your project is about
        """
        # Checking that scriptID and pName are strings
        if isinstance(scriptID, str) == False: 
            raise ValueError("appendProjectsTable(): Invalid scriptID variable type entered.")
        elif isinstance(pName, str) == False:
            raise ValueError("appendProjectsTable: Invalid pName entered")
        
        with self.conn:
            self.cur.execute("INSERT INTO projects ('scriptID','name','desc') VALUES (?,?,?)", [
                scriptID,
                pName,
                pDesc
            ])
        
        return "projectsInsert() successful."

    def printProjects(self):
        """Print a list of all projects."""
        with self.conn:
            self.cur.execute("""
                SELECT * FROM projects
            """)
            print(self.cur.fetchall())
        
        return "printProjects() successful."