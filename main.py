# Password manager with python
# Store url - username - password - note encrypted 

from cryptography.fernet import Fernet

message = "Hello world"

key = Fernet.generate_key()
print(key)
fernet = Fernet(key)

encMessage = fernet.encrypt(message.encode())

print("Original : ", message)
print("Encrypted : ", encMessage)