# Fundamentos de segurança

Base de conhecimento do GuardAI. Use estes conceitos para explicar uma análise de vulnerabilidade com os termos certos e em linguagem simples.

## Os quatro termos que mais se confundem

- **Ativo:** o que tem valor e precisa de proteção. Dados de clientes, senhas, o próprio sistema no ar.
- **Vulnerabilidade:** a fraqueza que permite um ataque. Exemplo: um login que cola o texto digitado dentro do comando SQL.
- **Ameaça:** quem ou o que pode explorar a fraqueza. Um atacante na internet, um robô automatizado, alguém de dentro mal-intencionado.
- **Risco:** a chance de a ameaça explorar a vulnerabilidade, combinada com o estrago que isso causaria.

Comparação para explicar: a casa é o ativo, a janela sem tranca é a vulnerabilidade, o ladrão é a ameaça, e o risco depende de a janela dar para a rua ou para um quintal fechado.

## Tríade CIA

- **Confidencialidade:** só quem deve vê o dado.
- **Integridade:** o dado não é alterado sem autorização.
- **Disponibilidade:** o sistema funciona quando precisam dele.

Ao avaliar o impacto, diga qual dos três a falha atinge.

## Impacto, probabilidade e severidade

- **Impacto:** o tamanho do estrago se a falha for explorada.
- **Probabilidade:** o quão fácil e provável é a exploração. Pesam quem controla a entrada, se o sistema está exposto na internet e se a falha é conhecida.
- **Severidade:** a combinação dos dois.

| Probabilidade \ Impacto | Baixo | Médio | Alto |
|---|---|---|---|
| **Alta** | Média | Alta | Crítica |
| **Média** | Baixa | Média | Alta |
| **Baixa** | Baixa | Baixa | Média |

Sempre justifique o nível escolhido em uma frase.

## OWASP Top 10

Lista mantida pela OWASP com as categorias de falha mais comuns em aplicações web, como controle de acesso quebrado, falhas de criptografia, injeção e configuração insegura. Use para classificar o achado e indicar onde a pessoa pode estudar mais.

## CWE

Catálogo que dá um número para cada tipo de fraqueza. Exemplo: CWE-89 é a injeção de SQL. Citar o CWE ajuda a pessoa a achar documentação sobre a falha.

## SQL Injection

Acontece quando o programa monta o comando SQL juntando texto digitado pelo usuário. O banco não consegue separar comando de dado, então a entrada pode mudar o sentido da consulta: entrar sem senha, ler dados de outras pessoas ou apagar registros.

**Correção principal:** consulta parametrizada, também chamada de prepared statement. O comando vai com lugares reservados, como `?`, e os valores vão separados. O banco trata o que foi digitado sempre como dado.

**Ajudam, mas não substituem:** validar a entrada, usar no banco um usuário com o mínimo de permissões e não mostrar erros do banco para o usuário.

## Boas práticas que aparecem em quase toda análise

- **Menor privilégio:** cada usuário e sistema só com as permissões de que precisa.
- **Defesa em profundidade:** várias camadas de proteção, para uma falha não derrubar tudo.
- **Senhas:** nunca guardar em texto puro. Guardar só o hash, com um algoritmo próprio para senhas, como bcrypt ou argon2.
- **Erros:** mensagem genérica para o usuário. O detalhe técnico vai para o log.
- **Logs:** registrar tentativas de login e ações sensíveis, sem gravar senhas.

## Ética

- Teste de segurança só em sistema próprio ou com autorização por escrito.
- Laboratório é para aprender a defender: o objetivo é entender a falha e corrigir.
- Achou uma falha num sistema de terceiros? O caminho é avisar o responsável (divulgação responsável), sem explorar.