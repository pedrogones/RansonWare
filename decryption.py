import os
import shutil
import pyAesCrypt
from pathlib import Path
import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog

# Define as pastas para descriptografar
folders_path = [
    str(os.path.join(Path.home(), "Downloads")),
    str(os.path.join(Path.home(), "Documents"))
]

# Obtém a chave de descriptografia
root = tk.Tk()
root.withdraw()
key = tkinter.simpledialog.askstring("Decryption Key", "Enter the decryption key:", parent=root)

# Descriptografa todos os arquivos em cada pasta
for folder_path in folders_path:
    for file in os.listdir(folder_path):
        bufferSize = 64 * 1024
        # Obtém o caminho do arquivo atual
        file_path = os.path.join(folder_path, file)
        if file.endswith(".aes"):
            # Descriptografa o arquivo
            pyAesCrypt.decryptFile(file_path, file_path[:-4], key, bufferSize)
            # Move o arquivo descriptografado para o destino
            destination_path = os.path.join(folder_path, "decrypted_" + file[:-4])
            shutil.move(file_path[:-4], destination_path)
            # Exclui o arquivo criptografado
            os.remove(file_path)

# Exibe uma mensagem informando que a descriptografia foi concluída
messagebox.showinfo("Decryption Complete", "All files in the folders have been decrypted.")
root.mainloop()
