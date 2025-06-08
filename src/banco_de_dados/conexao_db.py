import sqlite3
import pandas as pd

def conectar_bd(nome_bd="grãos.db"):
    return sqlite3.connect(nome_bd)

def criar_tabela_grãos(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS grãos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        area REAL,
        perimetro REAL,
        compacidade REAL,
        comprimento_nucleo REAL,
        largura_nucleo REAL,
        coef_assimetria REAL,
        comprimento_sulco REAL,
        classe INTEGER
    )
    """)
    conn.commit()

def inserir_dados(df, conn):
    df.to_sql("grãos", conn, if_exists='append', index=False)
