# ============================================================
#              DOCUMENTAÇÃO DO SISTEMA
# ============================================================

NOME DO SISTEMA:
Fluxus 

INTEGRANTES DO GRUPO:
- [João Pedro de Lira Tavares - 20250104501]
- [Andrey oliveira moura  - 20250104261]
- [Marcos Antônio José da Silva - 20250104600]
- [Guilherme da Silva Virginio - 20250144946]

DESCRIÇÃO GERAL:
Este sistema em Python permite controlar o estoque de ingredientes/produtos e gerenciar pedidos de mesas em um restaurante. O usuário pode cadastrar, atualizar e remover itens do estoque, criar pedidos com validação de disponibilidade, acompanhar status dos pedidos e visualizar um relatório geral com resumo de pedidos e alerta de estoque baixo. Os dados são persistidos em arquivo JSON, permitindo manter as informações entre execuções do programa.

PERSISTÊNCIA DE DADOS (ARQUIVO JSON):
O sistema utiliza o arquivo `restaurante_dados.json` para salvar e carregar as informações do estoque e dos pedidos.
- Ao iniciar o programa, a função `carregar_dados()` tenta ler o JSON.
- Se o arquivo não existir, o sistema cria o arquivo com os dados iniciais.
- Sempre que há alteração no estoque, criação de pedido ou mudança de status, a função `salvar_dados()` grava automaticamente os dados no JSON.
- Estrutura do arquivo: `{"estoque": [...], "pedidos": [...], "proximo_id": int}`.

EXPLICAÇÃO DO MENU:
O menu principal possui três áreas: Estoque, Pedidos e Relatório geral. No menu de estoque é possível listar itens, adicionar novos produtos, atualizar quantidades e remover itens. No menu de pedidos é possível criar novo pedido, listar pedidos, ver detalhes de um pedido específico e atualizar o status do pedido. A opção de relatório exibe indicadores gerais, como número total de pedidos, pedidos abertos, pedidos entregues, receita dos pedidos entregues e itens com quantidade crítica no estoque.

ESTRUTURA DE DADOS:
Os dados principais são armazenados em três variáveis globais e persistidos em JSON. `estoque` é uma lista de dicionários no formato `{"nome": str, "quantidade": float, "unidade": str, "preco": float}`. `pedidos` é uma lista de dicionários no formato `{"id": int, "mesa": str, "itens": list, "total": float, "status": str}`, em que cada item de `itens` possui `nome`, `quantidade`, `unidade`, `preco_unit` e `subtotal`. `proximo_id` é um inteiro usado para gerar IDs sequenciais de pedidos.

FUNCIONALIDADES (FUNÇÕES):

- Nome da Função: `carregar_dados()`
  - Parâmetros: Nenhum.
  - Retorno: Nenhum (`None`).
  - Descrição: Lê o arquivo `restaurante_dados.json` e carrega `estoque`, `pedidos` e `proximo_id` para memória. Em caso de ausência do arquivo, cria o JSON com os dados atuais.

- Nome da Função: `salvar_dados()`
  - Parâmetros: Nenhum.
  - Retorno: Nenhum (`None`).
  - Descrição: Salva o estado atual de `estoque`, `pedidos` e `proximo_id` no arquivo `restaurante_dados.json`.

- Nome da Função: `separador()`
  - Parâmetros: Nenhum.
  - Retorno: Nenhum (`None`).
  - Descrição: Imprime uma linha de separação visual na tela.

- Nome da Função: `cabecalho(titulo)`
  - Parâmetros: `titulo` (texto do título da seção).
  - Retorno: Nenhum (`None`).
  - Descrição: Exibe um cabeçalho formatado com linha superior e inferior.

- Nome da Função: `pausar()`
  - Parâmetros: Nenhum.
  - Retorno: Nenhum (`None`).
  - Descrição: Aguarda o usuário pressionar ENTER para continuar.

- Nome da Função: `listar_estoque()`
  - Parâmetros: Nenhum.
  - Retorno: Nenhum (`None`).
  - Descrição: Mostra todos os itens do estoque com nome, quantidade, unidade e preço unitário; sinaliza itens com quantidade menor que 5.

- Nome da Função: `adicionar_item_estoque()`
  - Parâmetros: Nenhum.
  - Retorno: Nenhum (`None`).
  - Descrição: Solicita dados de um novo item, valida entradas, evita nomes duplicados e adiciona o item ao estoque.

- Nome da Função: `atualizar_estoque()`
  - Parâmetros: Nenhum.
  - Retorno: Nenhum (`None`).
  - Descrição: Permite escolher um item do estoque e alterar sua quantidade.

- Nome da Função: `remover_item_estoque()`
  - Parâmetros: Nenhum.
  - Retorno: Nenhum (`None`).
  - Descrição: Permite remover um item do estoque após confirmação do usuário.

- Nome da Função: `listar_estoque_breve()`
  - Parâmetros: Nenhum.
  - Retorno: Nenhum (`None`).
  - Descrição: Exibe uma versão resumida do estoque para apoio a outras rotinas.

- Nome da Função: `novo_pedido()`
  - Parâmetros: Nenhum.
  - Retorno: Nenhum (`None`).
  - Descrição: Cria um novo pedido para uma mesa, adiciona itens com validação de quantidade disponível, desconta do estoque, calcula subtotais/total e registra o pedido com ID único.

- Nome da Função: `listar_pedidos()`
  - Parâmetros: Nenhum.
  - Retorno: Nenhum (`None`).
  - Descrição: Lista todos os pedidos registrados com ID, mesa, status e valor total.

- Nome da Função: `ver_detalhes_pedido()`
  - Parâmetros: Nenhum.
  - Retorno: Nenhum (`None`).
  - Descrição: Exibe os detalhes completos de um pedido específico informado pelo ID.

- Nome da Função: `atualizar_status_pedido()`
  - Parâmetros: Nenhum.
  - Retorno: Nenhum (`None`).
  - Descrição: Permite alterar o status de um pedido entre opções predefinidas (Aberto, Em preparo, Pronto, Entregue, Cancelado).

- Nome da Função: `listar_pedidos_breve()`
  - Parâmetros: Nenhum.
  - Retorno: Nenhum (`None`).
  - Descrição: Mostra uma listagem resumida dos pedidos, usada internamente em outras funções.

- Nome da Função: `relatorio()`
  - Parâmetros: Nenhum.
  - Retorno: Nenhum (`None`).
  - Descrição: Exibe resumo geral com métricas de pedidos e receita de pedidos entregues, além da lista de itens com estoque abaixo de 5 unidades.

- Nome da Função: `menu_estoque()`
  - Parâmetros: Nenhum.
  - Retorno: Nenhum (`None`).
  - Descrição: Controla o submenu de operações de estoque por laço de repetição.

- Nome da Função: `menu_pedidos()`
  - Parâmetros: Nenhum.
  - Retorno: Nenhum (`None`).
  - Descrição: Controla o submenu de operações de pedidos por laço de repetição.

- Nome da Função: `menu_principal()`
  - Parâmetros: Nenhum.
  - Retorno: Nenhum (`None`).
  - Descrição: Exibe o menu principal e direciona para os submenus de estoque, pedidos e relatório.

COMO EXECUTAR O PROGRAMA:
1. Abra um terminal na pasta do projeto.
2. Execute o comando:

```bash
python restaurante.py
```

3. Use os menus exibidos na tela para operar o sistema.
