# Projeto de Criptografia e Descriptografia
---

Este projeto demonstra a criptografia e descriptografia de arquivos usando o algoritmo AES (Advanced Encryption Standard). O projeto inclui dois scripts Python: um para criptografar arquivos e adicionar uma mensagem de resgate e outro para descriptografar os arquivos criptografados.

## Configuração do Ambiente

### 1. **Instalação do Ambiente**

Certifique-se de que o Python 3 está instalado em seu sistema e que a biblioteca `cryptography` está disponível. Você pode instalar a biblioteca usando o `pip`:

pip install cryptography


### 1. **Criação do Ambiente de Teste**

1. **Crie o Diretório de Teste**

   Crie um diretório para os arquivos de teste e navegue até ele:

   mkdir ~/testandoRansonWare
   cd ~/testandoRansonWare

2. **Crie Arquivos de Teste**

   Crie alguns arquivos de texto simples para testar a criptografia. Por exemplo:

   echo "Este é o conteúdo do teste1." > teste1.txt  <br>
   echo "Este é o conteúdo do teste2." > teste2.txt


3. **Crie o Arquivo de Chave**

   Crie um arquivo para armazenar a chave de criptografia:

   echo "6a2c3d4e5f6789ab123c456d7890ef12" > ~/ransonware/key.txt

### 3. **Execução dos Scripts**

1. **Execute o Script de Criptografia**

   Navegue até o diretório onde o script `ransonware.py` está localizado e execute-o:

   python3 ransonware.py

   Isso criptografará todos os arquivos no diretório `~/testandoRansonWare` que não possuem a extensão `.aes` e adicionará uma mensagem de resgate ao final dos arquivos criptografados.

2. **Execute o Script de Descriptografia**

   Navegue até o diretório onde o script `decryption.py` está localizado e execute-o:

   python3 decryption.py

   Isso descriptografará todos os arquivos no diretório `~/testandoRansonWare` que possuem a extensão `.aes` e salvará o conteúdo descriptografado em novos arquivos com a extensão `.decrypted.txt`.

### 4. **Verificação**

- **Verifique se os arquivos criptografados foram gerados corretamente** e se o conteúdo deles corresponde ao esperado.
- **Verifique se os arquivos descriptografados correspondem ao conteúdo original dos arquivos antes da criptografia**.
