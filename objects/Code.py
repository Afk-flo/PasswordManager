# Object code py 
from cryptography.fernet import Fernet

class Code:

    def __init__(self, title, username, password, url, note):
        self.title = title,
        self.username = username,
        self.password = password,
        self.url = url,
        self.note = note
        pass

    def encryptPassword(self, key):
        fernet = Fernet(key)
        self.password = fernet.encrypt(self.password.encode())
        pass

    def decryptPassword(self, key):
        fernet = Fernet(key)
        self.password = fernet.decrypt(self.password.decode())
        pass

    