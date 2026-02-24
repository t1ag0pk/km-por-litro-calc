import sqlite3

def inicializar_banco():

    # 1. Estabelece a conexão (cria o arquivo se não existir)
    conexao = sqlite3.connect('controle_abastecimento.db')
    
    # 2. Cria o cursor para interagir com o banco
    cursor = conexao.cursor()
    
    # 3. O comando SQL para criar a tabela
    # Formato: nome_da_coluna TIPO_DE_DADO
    sql = """
    CREATE TABLE IF NOT EXISTS abastecimentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT NOT NULL,
        km REAL NOT NULL,
        valor_litro REAL NOT NULL,
        quantidade_litros REAL NOT NULL,
        valor_total REAL NOT NULL
    )
    """
    
    # 4. Executa o comando
    cursor.execute(sql)
    
    # 5. Salva (commit) e fecha
    conexao.commit()
    conexao.close()

def salvar_abastecimento(data, km, valor_litro, litros):

    conexao = sqlite3.connect('controle_abastecimento.db')
    cursor = conexao.cursor()

    inserir = "INSERT INTO abastecimentos (data, km, valor_litro, quantidade_litros, valor_total) VALUES (?, ?, ?, ?, ?)"
    dados = (data, km, valor_litro, litros, (valor_litro*litros))

    cursor.execute(inserir, dados)
    conexao.commit()
    conexao.close()

def buscar_dados(filtro_sql=""):
    conexao = sqlite3.connect('controle_abastecimento.db')
    cursor = conexao.cursor()
    
    # A base do comando é sempre a mesma
    sql = f"SELECT * FROM abastecimentos {filtro_sql}"
    
    cursor.execute(sql)
    dados = cursor.fetchall()
    
    conexao.close()
    return dados

def busca_por_id(busca_id):
    conexao = sqlite3.connect('controle_abastecimento.db')
    cursor =conexao.cursor()

    sql = f"SELECT * FROM abastecimentos WHERE id = ?"

    cursor.execute(sql, (busca_id,))

    conexao.commit()
    resultado = cursor.fetchone()
    conexao.close()
    return resultado



def excluir_dados(id_para_excluir):
    conexao = sqlite3.connect('controle_abastecimento.db')
    cursor =conexao.cursor()

    excluir = "DELETE FROM abastecimentos WHERE id = ?"

    cursor.execute(excluir, (id_para_excluir,))

    conexao.commit()
    linhas_afetadas = cursor.rowcount
    conexao.close()
    return linhas_afetadas

if __name__ == "__main__":
    inicializar_banco()
    print("Banco de dados inicializado com sucesso!")