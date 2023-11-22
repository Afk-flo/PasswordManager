# EncryptManager is the utils tools who managed the encryption system
from cryptography.fernet import Fernet

# Create the key and store it in the .env file 
def init():
    try :
        file = open('../.env', 'r')
        data = file.readline(size=-1)
        file.close()
        if data is None :
            try :
                file = open('../env', 'w')
                # Generating the symetrical key
                key = Fernet.generate_key()
                file.write("KEY=", key)
            except :    
                PermissionError("[-] Error : Couldn't write in the .env file. [-]")
    except:
        FileNotFoundError("[-] Error : Couldn't open or modify the .env file. [-]")
        exit()
    # At the end, we're closing the file and keeping the key
    finally:
        file.close() 
        return key



# Encrypt the data using the fernet key 
def encryptData(key, data):
    try:
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data.encode())
        return encrypted_data
    except:
        Exception("[-] Error, couldn't encrypt the data. [-]")


# Decrypt the data using the fernet key 