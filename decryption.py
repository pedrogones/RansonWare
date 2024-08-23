from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

def read_key_from_file(file_path):
    with open(file_path, 'r') as f:
        return f.read().strip()

# Função para descriptografar o arquivo
def decrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()
    
    iv = encrypted_data[:16]  # IV é o primeiro bloco de 16 bytes
    data = encrypted_data[16:]
    
    cipher = Cipher(algorithms.AES(bytes.fromhex(key)), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(data) + decryptor.finalize()
    
    # Remover padding
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()
    
    decrypted_file_path = file_path.replace('.aes', '.decrypted.txt')
    with open(decrypted_file_path, 'wb') as f:
        f.write(data)
    
    print(f"Arquivo descriptografado salvo em: {decrypted_file_path}")

# Caminho do diretório onde os arquivos serão processados
target_directory = os.path.expanduser("~/testandoRansonWare")

# Caminho do arquivo de chave
key_file_path = os.path.join(os.path.expanduser("~"), 'ransonware', 'key.txt')
key = read_key_from_file(key_file_path)

# Descriptografa arquivos
for root, dirs, files in os.walk(target_directory):
    for file in files:
        if file.endswith(".aes"):
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)
