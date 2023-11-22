## All the database function in order to store, retreive and delete password
import sqlite3
import uuid

# Create database 
def createDatabase():
    con = sqlite3.connect("passman.db")
    print("Database opened - Creation of the database")
    print("Please wait ..")
    # Table creation (we only need one tbh)
    con.execute('''''CREATE TABLE Code
                (Id INT PRIMARY KEY NOT NULL,
                Title TEXT,
                Username TEXT,
                Password TEXT,
                Url TEXT,
                Note TEXT,
                );
    ''')
    print("Table created successfully, you can now use the app")
    return con

# Try to connect to the database, if failed exit
def connectDatabase():
    try:
        con = sqlite3.connect('passman.db')
        print("Database connected successfully")
        return con
    except:
        print("Error in the database connexion - Try to setup a new database or to fix it")
        exit()


# Insert a new code
def addCode(con, code):
    id = uuid.uuid4()

    # Foreach code pour éviter erreur sur nul
    for attr, data in code.__dict__.items():
        if data is None :
            data = ""
        if attr == "password" :
            data = Code

    # Input 
    try :
        con.execute("INSERT INTO Code (Id,Title,Username,Pasword,Url,Note) VALUES ()")
        print("[+] - Data registrered successfully")
    except:
        print("[-] - Error, we couldn't save this code.")
    pass



# Read the database info 
def readDatabase(con):
    data = con.execute("select * from Code")
    return data

# Get One entry
def getOne(con, id):
    data = con.execute("select * from Code where Id = %i", id)
    return data

# Update one
def update(con, code):
    pass

# Delete one
def delete(con, id):
    try :
        con = con.execute("delete * from Code where id = %i", id)
        print("[+] - Success, the code has been deleted")
    except:
        print("[-] Error - We couldn't delete the specified object")
    
def close(con):
    try:
        con.close()
        print("[+] - Database fermée. Bonne journée.")
    except:
        Exception("[-] - Error during the database closing.")


