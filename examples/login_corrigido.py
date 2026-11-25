"""
Exemplo de laboratório: o mesmo login, CORRIGIDO com consulta parametrizada.
O comando SQL e os valores vão separados para o banco, então o que a pessoa
digita é sempre tratado como dado, nunca como parte do comando.

A senha continua em texto puro só para manter o exemplo pequeno e focado na injeção.
Num sistema de verdade, guarde apenas o hash da senha (bcrypt ou argon2, por exemplo).
"""
import sqlite3


def criar_banco():
    """Cria um banco temporário, só na memória, com um usuário de teste."""
    conexao = sqlite3.connect(":memory:")
    conexao.execute("CREATE TABLE usuarios (usuario TEXT, senha TEXT)")
    conexao.execute("INSERT INTO usuarios VALUES ('ana', 'senha-de-teste-123')")
    conexao.commit()
    return conexao


def login(conexao, usuario, senha):
    # CORREÇÃO: cada "?" é um lugar reservado. Os valores vão no segundo argumento,
    # separados do comando, e o banco nunca os interpreta como SQL.
    consulta = "SELECT 1 FROM usuarios WHERE usuario = ? AND senha = ?"
    return conexao.execute(consulta, (usuario, senha)).fetchone() is not None


if __name__ == "__main__":
    banco = criar_banco()
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    print("Acesso liberado" if login(banco, usuario, senha) else "Acesso negado")