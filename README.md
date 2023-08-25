<p align="center">
<img src="docs/assets/logo.png" align="center" width="700">
</p>

---

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![GitHub repo size](https://img.shields.io/github/repo-size/davitorress/Osiris-web)
![GitHub](https://img.shields.io/github/license/davitorress/Osiris-web)
![GitHub language count](https://img.shields.io/github/languages/count/davitorress/Osiris-web)
![GitHub last commit](https://img.shields.io/github/last-commit/davitorress/Osiris-web)

# Tecnologias utilizadas

<p align="center">
<img src="https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white"> 
<img src="https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white"> 
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"> 
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"> 
<img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white">
</p>

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
