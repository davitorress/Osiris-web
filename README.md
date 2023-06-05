<img src="docs/assets/logo.png" align="center" width="700">

---

# Instruções de Instalação

## Banco de dados noSQL MongoDB

- Efetua o download e instalação do MongoDB [aqui](https://www.mongodb.com/try/download/community).

- Baixe as coleções [deste repositório](https://github.com/mfelipegs/osiris-database/tree/main/db/collections) e importe-as em seu MongoDB, em um novo banco com o nome `Osiris`.

## Preparação da Venv (Virtual Environment)

- Certifique-se de que sua máquina esteja com a ferramenta de gerenciamento de pacotes Python [pip](https://pypi.org/project/pip/).

- Instale o pacote virtualenv, com o comando:

  `pip install virtualenv`

- Após instalar o virtualenv, crie a sua virtual environment e a ative com os seguintes comandos:

  ### Windows

  `virtualenv venv_osiris`

  `venv_osiris\Scripts\activate.bat`

  ### Linux e MacOS

  `virtualenv venv_osiris`

  `source venv_osiris/bin/activate`

- Agora que a virtualenv está ativada, instale as dependências do projeto:

  `pip install -r requirements.txt`

Após isso, o projeto em Flask, Osiris, está pronto para ser executado.
