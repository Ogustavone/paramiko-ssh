import json, os, time
from paramiko import SSHClient, AutoAddPolicy, RSAKey

class ConnectSSH:
  """
  Métodos:
    sendFile(src, dst) -> enviar arquivos para o servidor.
    downloadFile(src, dst) -> receber arquivos para o computador local.
    sendCommand(command) -> enviar comandos para o servidor.
    showScreen() -> mostrar as instâncias abertas no Screen.
  """
  def __init__(self, user):
    self.user = user

    with open('config.json') as file:
      data = json.load(file)
      if user not in data:
        raise Exception('User not found!')
      elif not os.path.exists(data[user]['rsa_key']):
        raise Exception('RSA key not found!')

    self.hostname = json.load(open('config.json'))[user]['hostname']
    self.ip = json.load(open('config.json'))[user]['ip']
    self.port = json.load(open('config.json'))[user]['port']
    self.rsa_key = json.load(open('config.json'))[user]['rsa_key']
    self.private_key = RSAKey.from_private_key_file(self.rsa_key)
    
    self.client = SSHClient()
    self.client.set_missing_host_key_policy(AutoAddPolicy())

  def sendFile(self, src: str, dst):
    """Usado para enviar arquivos para o servidor.
    Args:
      src (string): Caminho do arquivo a ser enviado.
      dst (string): Destino do arquivo no servidor.
    """
    self.client.connect(hostname=self.ip, port=self.port, username=self.hostname, pkey=self.private_key)

    os.system(f'scp -i {self.rsa_key} {src} {self.hostname}@{self.ip}:{dst}')
    print('Enviando...')
    time.sleep(3)
    print(f"[Comando] cd {dst} && ls")
    stdin, stdout, stderr = self.client.exec_command(f'cd {dst} && ls')
    print(stdout.read().decode())
    self.client.close()

  def downloadFile(self, src, dst):
    """Usado para receber arquivos para o computador local.
    Args:
      src (string): Caminho do arquivo a ser recebido.
      dst (string): Destino do arquivo no computador.
    """
    os.system(f'scp -i {self.rsa_key} {self.hostname}@{self.ip}:{src} {dst}')
    print(f'Arquivo {src} recebido com sucesso!')
  
  def sendCommand(self, command: str):
    """Usado para enviar comandos para o servidor."""
    self.client.connect(hostname=self.ip, port=self.port, username=self.hostname, pkey=self.private_key)
    stdin, stdout, stderr = self.client.exec_command(command)
    print(stdout.read().decode())
    self.client.close()

  def showScreen(self):
    """Usado para mostrar as instâncias abertas no Screen."""
    self.client.connect(hostname=self.ip, port=self.port, username=self.hostname, pkey=self.private_key)
    stdin, stdout, stderr = self.client.exec_command('screen -ls')
    print(stdout.read().decode())
    self.client.close()

# Exemplo de uso
"""
client = ConnectSSH('example-name')
client.showScreen()
"""
