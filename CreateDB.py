import sqlite3
from util.Color import *

def criarBanco():
    print(YELLOW + "Criando banco de dados...")
    try:
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE pessoa(
                id integer PRIMARY KEY AUTOINCREMENT,
                nome varchar(100) NOT NULL,
                cpf varchar(50) NOT NULL UNIQUE,
                senha varchar(20) NOT NULL
            );
        """)

        cursor.execute("""
            CREATE TABLE paciente(
                id integer PRIMARY KEY AUTOINCREMENT,
                pessoa_id integer NOT NULL,
                plano_saude boolean NOT NULL,
                FOREIGN KEY(pessoa_id) REFERENCES pessoa(id)
            );
        """)

        cursor.execute("""
            CREATE TABLE medico(
                id integer PRIMARY KEY AUTOINCREMENT,
                pessoa_id integer NOT NULL,
                especializacao varchar(20) NOT NULL,
                salario float NOT NULL,
                FOREIGN KEY(pessoa_id) REFERENCES pessoa(id)
            );
        """)

        cursor.execute("""
            CREATE TABLE secretario(
                id integer PRIMARY KEY AUTOINCREMENT,
                pessoa_id integer NOT NULL,
                salario float NOT NULL,
                FOREIGN KEY(pessoa_id) REFERENCES pessoa(id)
            );
        """)

        cursor.execute("""
            CREATE TABLE balconista(
                id integer PRIMARY KEY AUTOINCREMENT,
                pessoa_id integer NOT NULL,
                salario float NOT NULL,
                FOREIGN KEY(pessoa_id) REFERENCES pessoa(id)
            );
        """)

        cursor.execute("""
            CREATE TABLE consulta(
                id integer PRIMARY KEY AUTOINCREMENT,
                preco float,
                data date,
                paciente_id NOT NULL,
                medico_id NOT NULL,
                realizada boolean default false,
                paga boolean default false,
                FOREIGN KEY(paciente_id) REFERENCES paciente(id),
                FOREIGN KEY(medico_id) REFERENCES medico(id)
            );
        """)

        cursor.execute("""
            CREATE TABLE receita(
                id integer PRIMARY KEY AUTOINCREMENT,
                indicacoes varchar(50) NOT NULL,
                medicamentos varchar(50) NOT NULL,
                paciente_id integer NOT NULL,
                medico_id integer NOT NULL,
                FOREIGN KEY(paciente_id) REFERENCES paciente(id),
                FOREIGN KEY(medico_id) REFERENCES medico(id)
            );
        """)

        print(GREEN + BOLD + "Banco de dados criado!")
    except sqlite3.OperationalError as err:
        print(RED + str(err))
        print(YELLOW + "Banco de dados já existente.")
    except Exception as err:
        print(RED + BOLD + err.args[0])