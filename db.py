import sqlite3


def criar():
    conn = sqlite3.connect('volei.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS volei(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(255) NOT NULL,
            posicao VARCHAR(3) NOT NULL,
            altura REAL NOT NULL);
    """)

    conn.close()


def novo_atleta(nome, posicao, altura):
    conn = sqlite3.connect('volei.db')
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO volei(nome, posicao, altura)
        VALUES(?, ?, ?);
    """, (nome, posicao, altura))
    conn.commit()
    conn.close()


def listar_atleta():
    conn = sqlite3.connect('volei.db')
    cursor = conn.cursor()
    values = cursor.execute("SELECT * FROM volei")
    resultado = []
    for row in values:
        resultado.append({
            'id': row[0],
            'nome': row[1],
            'posicao': row[2],
            'altura': row[3],
        })
    conn.close()
    return resultado


def atualiza_atleta(id, nome, posicao, altura):
    conn = sqlite3.connect('volei.db')
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE volei
        SET nome=?, posicao=?, altura=?
        WHERE id=?;
        """,
        (nome, posicao, altura, id)
    )
    conn.commit()
    conn.close()


def remove_atleta(id):
    conn = sqlite3.connect('volei.db')
    cursor = conn.cursor()
    cursor.execute(
        """
        DELETE FROM volei
        WHERE id=?;
        """,
        (id,)
    )
    conn.commit()
    conn.close()



def detalha_atleta(id):
    conn = sqlite3.connect('volei.db')
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT *
        FROM volei
        WHERE id=?;
        """,
        (id,)
    )
    item = cursor.fetchone()
    conn.close()
    if item is None:
        return None
    return {
        'id': item[0],
        'nome': item[1],
        'posicao': item[2],
        'altura': item[3],
    }


if __name__=='__main__':
    criar()
