"""
Compara as duas versões do login.
O teste usa um nome com aspa simples, como "d'avila": na versão vulnerável,
essa aspa quebra o comando SQL, o que prova que a entrada vira parte do comando.

Rode a partir da pasta do projeto:  python examples/teste_login.py
"""
import sqlite3

import login_corrigido
import login_vulneravel

SENHA_CERTA = "senha-de-teste-123"


def testar(modulo):
    banco = modulo.criar_banco()
    print(f"\n{modulo.__name__}")
    print("  senha certa: ", "entrou" if modulo.login(banco, "ana", SENHA_CERTA) else "não entrou")
    print("  senha errada:", "entrou" if modulo.login(banco, "ana", "errada") else "não entrou")
    try:
        entrou = modulo.login(banco, "d'avila", "qualquer")
        print("  nome com aspa simples:", "entrou" if entrou else "não entrou, tratado como dado")
    except sqlite3.OperationalError as erro:
        print(f"  nome com aspa simples: ERRO NO SQL ({erro}), a entrada mudou o comando")


if __name__ == "__main__":
    testar(login_vulneravel)
    testar(login_corrigido)