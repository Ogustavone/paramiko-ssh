# Projeto de Conexão SSH simplificado com Paramiko
Este projeto utiliza a biblioteca Paramiko para estabelecer conexões SSH com servidores remotos. Ele permite que você execute comandos, envie e receba arquivos, e visualize as instâncias abertas no Screen.

## Arquivos importantes
- sshParamiko.py: contém a classe ConnectSSH que implementa as funcionalidades do projeto
- config.json: contém as configurações de conexão para os servidores remotos

## Como usar
- Edite o arquivo config.json para adicionar ou modificar as configurações de conexão.
- Importe a classe ConnectSSH no seu script Python e crie uma instância dela, passando o nome do usuário como parâmetro.
- Use os métodos da classe para executar comandos, enviar e receber arquivos, e visualizar as instâncias abertas no Screen.

Exemplo:

```python
from sshParamiko import ConnectSSH

client = ConnectSSH('oracle-virtualMachine')
client.showScreen()
```
