# Skill: análise de vulnerabilidades

Essa skill faz o GuardAI analisar um código como alguém de AppSec faria numa revisão: aponta a linha com problema, explica o porquê, avalia o risco e mostra a correção.

## Quando ela entra em ação

Não precisa chamar pelo nome. Basta colar um código e perguntar algo como:

- "Esse login tem alguma vulnerabilidade?"
- "Revisa a segurança dessa função pra mim."
- "Isso aqui está vulnerável a SQL Injection?"

## O que ela entrega

Sempre na mesma ordem: resumo, onde está a falha, classificação (OWASP e CWE), risco (impacto, probabilidade e severidade), correção com antes e depois, como verificar, outros achados e o que estudar a seguir.

## Limites

A skill é defensiva. Ela explica a falha e como corrigir, mas não monta ataque nem ensina a invadir sistema de outra pessoa. Se você não disser onde o código roda ou se tem autorização para testar, ela pergunta antes.

## Para testar

Em `examples/` tem um login vulnerável a SQL Injection, a versão corrigida com consulta parametrizada e um teste que compara as duas. O roteiro está em `docs/teste-sql-injection.md`.