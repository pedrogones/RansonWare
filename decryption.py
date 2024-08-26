from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def read_key_from_file(file_path):
    """Lê a chave de criptografia a partir de um arquivo."""
    with open(file_path, 'r') as f:
        return f.read().strip()

def decrypt_file(file_path, key):
    """Descriptografa um arquivo criptografado e salva o resultado em um novo arquivo."""
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()

    # Extrai o IV (vetor de inicialização) dos primeiros 16 bytes do arquivo criptografado
    iv = encrypted_data[:16]

    # Localiza o índice do separador de mensagem no arquivo criptografado
    sep_index = encrypted_data.find(b'---END---', 16)
    if sep_index == -1:
        raise ValueError("Separator not found in encrypted data.")

    # Divide os dados criptografados e a mensagem de resgate
    data = encrypted_data[16:sep_index]

    # Configura o objeto Cipher com AES no modo CFB
    cipher = Cipher(algorithms.AES(bytes.fromhex(key)), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Descriptografa os dados
    decrypted_data = decryptor.update(data) + decryptor.finalize()

    # Cria o caminho para o arquivo descriptografado
    decrypted_file_path = file_path.replace('.aes', '')

    # Salva os dados descriptografados no arquivo
    with open(decrypted_file_path, 'wb') as f:
        f.write(decrypted_data)

    # Remove o arquivo criptografado original
    os.remove(file_path)

    print(f"Arquivo descriptografado salvo em: {decrypted_file_path}")

# Diretório onde os arquivos criptografados estão localizados
target_directory = os.path.expanduser("~/TesteRansonware")

# Caminho do arquivo que contém a chave de criptografia
key_file_path = os.path.join(os.path.expanduser("~"), 'ransonware', 'key.txt')

# Lê a chave de criptografia do arquivo
key = read_key_from_file(key_file_path)

# Itera sobre todos os arquivos no diretório alvo
for root, dirs, files in os.walk(target_directory):
    for file in files:
        # Descriptografa arquivos que têm a extensão .aes
        if file.endswith(".aes"):
            file_path = os.path.join(root, file)
            try:
                decrypt_file(file_path, key)
            except Exception as e:
                print(f"Erro ao descriptografar o arquivo {file_path}: {e}")
