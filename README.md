<h1 align="center" id="titulo">Appointment manager</h1>

<p align="center" id="badges">
<img src="https://img.shields.io/badge/STATUS-CONCLU%C3%8DDO-GREEN?style=for-the-badge">
<img src="https://img.shields.io/badge/LICENSE-MIT-GREEN?style=for-the-badge"/>
</p>

## Índice 
* [Descrição do projeto](#descrição-do-projeto)
* [Layout da aplicação](#layout-da-aplicação)
* [Acesso ao projeto](#acesso-ao-projeto)
* [Tecnologias utilizadas](#tecnologias-utilizadas)
* [Licença](#licença)

## Descrição do projeto
<p align="justify">
Este projeto é uma aplicação de gerenciamento de consultas médicas. A aplicação permite o agendamento, atualização, exclusão e visualização de consultas agendadas, com funcionalidades adicionais para validação de dados e controle de horários disponíveis.
</p>

## Layout da aplicação

<p align="center">
    <img src="images/layout.png">
</p>

## Acesso ao projeto

Siga as etapas abaixo:
1. No terminal, clone o projeto:
    ```
    git clone https://github.com/Emmanuelly-Silva/appointment-manager.git
    ```

2. Mude para o diretório do projeto clonado:
    ```
    cd appointment-manager
    ```

3. Crie um ambiente virtual para isolar as dependências do projeto:
    ```
    python -m venv venv
    ```

4. Ative o ambiente virtual:
    - No Windows:
        ```
        venv\Scripts\activate
        ```
    - No macOS e Linux:
        ```
        source venv/bin/activate
        ```
5. Instale as dependências do projeto:
    ```
    pip install -r requirements.txt
    ```

6. Rode os comandos iniciais:
    ```
    python db_setup.py
    python main.py
    ```

## Tecnologias utilizadas
<p>
<img src="https://img.shields.io/badge/Python-3.11.1-blue?style=for-the-badge&logo=python&logoColor=yellow">
<img src="https://img.shields.io/badge/Tkinter-GUI-blue?style=for-the-badge&logo=python&logoColor=yellow">
<img src="https://img.shields.io/badge/Sqlite3-blue?style=for-the-badge&logo=sqlite">
</p>

## Licença

The [MIT License](LICENSE) (MIT)

Copyright :copyright: 2024 - Appointment manager
