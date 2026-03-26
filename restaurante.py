import json

ARQUIVO_DADOS = "restaurante_dados.json"

estoque = [
    {"nome": "Arroz",        "quantidade": 50, "unidade": "kg",  "preco": 5.00},
    {"nome": "Feijão",       "quantidade": 30, "unidade": "kg",  "preco": 7.50},
    {"nome": "Frango",       "quantidade": 20, "unidade": "kg",  "preco": 18.00},
    {"nome": "Óleo",         "quantidade": 10, "unidade": "L",   "preco": 9.00},
    {"nome": "Sal",          "quantidade": 15, "unidade": "kg",  "preco": 2.00},
    {"nome": "Refrigerante", "quantidade": 48, "unidade": "un",  "preco": 5.00},
    {"nome": "Água",         "quantidade": 60, "unidade": "un",  "preco": 2.50},
]

pedidos = []
proximo_id = 1


def carregar_dados():
    global estoque, pedidos, proximo_id
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        estoque_carregado = dados.get("estoque", estoque)
        pedidos_carregados = dados.get("pedidos", [])
        proximo_id_carregado = dados.get("proximo_id", 1)

        if isinstance(estoque_carregado, list) and isinstance(pedidos_carregados, list) and isinstance(proximo_id_carregado, int):
            estoque = estoque_carregado
            pedidos = pedidos_carregados
            proximo_id = proximo_id_carregado
            print("  Dados carregados do arquivo JSON.")
    except FileNotFoundError:
        salvar_dados()
    except (json.JSONDecodeError, OSError, TypeError):
        print("  Aviso: não foi possível carregar o arquivo JSON. Usando dados padrão.")


def salvar_dados():
    dados = {
        "estoque": estoque,
        "pedidos": pedidos,
        "proximo_id": proximo_id,
    }
    try:
        with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=2)
    except OSError:
        print("  Aviso: erro ao salvar dados no arquivo JSON.")




def separador():
    print("-" * 50)

def cabecalho(titulo):
    separador()
    print(f"  {titulo}")
    separador()

def pausar():
    input("\nPressione ENTER para continuar...")




def listar_estoque():
    cabecalho("ESTOQUE ATUAL")
    if not estoque:
        print("  Nenhum item no estoque.")
    else:
        print(f"  {'#':<4} {'Nome':<20} {'Qtd':<8} {'Un.':<6} {'Preço Unit.'}")
        separador()
        for i, item in enumerate(estoque):
            alerta = " ⚠ BAIXO" if item["quantidade"] < 5 else ""
            print(f"  {i+1:<4} {item['nome']:<20} {item['quantidade']:<8} {item['unidade']:<6} R$ {item['preco']:.2f}{alerta}")
    pausar()

def adicionar_item_estoque():
    cabecalho("ADICIONAR ITEM AO ESTOQUE")
    nome = input("  Nome do item: ").strip()
    if not nome:
        print("  Nome inválido.")
        pausar()
        return


    for item in estoque:
        if item["nome"].lower() == nome.lower():
            print(f"  '{nome}' já existe no estoque. Use 'Atualizar quantidade'.")
            pausar()
            return

    try:
        quantidade = float(input("  Quantidade: "))
        unidade    = input("  Unidade (kg, L, un...): ").strip()
        preco      = float(input("  Preço unitário (R$): "))
    except ValueError:
        print("  Valor inválido.")
        pausar()
        return

    estoque.append({"nome": nome, "quantidade": quantidade, "unidade": unidade, "preco": preco})
    salvar_dados()
    print(f"  '{nome}' adicionado com sucesso!")
    pausar()

def atualizar_estoque():
    listar_estoque_breve()
    cabecalho("ATUALIZAR QUANTIDADE")
    try:
        idx = int(input("  Número do item: ")) - 1
        if idx < 0 or idx >= len(estoque):
            print("  Item inválido.")
            pausar()
            return
        qtd = float(input("  Nova quantidade: "))
    except ValueError:
        print("  Valor inválido.")
        pausar()
        return

    estoque[idx]["quantidade"] = qtd
    salvar_dados()
    print(f"  Quantidade de '{estoque[idx]['nome']}' atualizada para {qtd} {estoque[idx]['unidade']}.")
    pausar()

def remover_item_estoque():
    listar_estoque_breve()
    cabecalho("REMOVER ITEM DO ESTOQUE")
    try:
        idx = int(input("  Número do item: ")) - 1
        if idx < 0 or idx >= len(estoque):
            print("  Item inválido.")
            pausar()
            return
    except ValueError:
        print("  Valor inválido.")
        pausar()
        return

    confirmacao = input(f"  Remover '{estoque[idx]['nome']}'? (s/n): ").lower()
    if confirmacao == "s":
        removido = estoque.pop(idx)
        salvar_dados()
        print(f"  '{removido['nome']}' removido do estoque.")
    else:
        print("  Operação cancelada.")
    pausar()

def listar_estoque_breve():
    separador()
    print(f"  {'#':<4} {'Nome':<20} {'Qtd':<8} {'Un.'}")
    separador()
    for i, item in enumerate(estoque):
        print(f"  {i+1:<4} {item['nome']:<20} {item['quantidade']:<8} {item['unidade']}")
    separador()




def novo_pedido():
    global proximo_id
    cabecalho("NOVO PEDIDO")

    mesa = input("  Número da mesa: ").strip()
    if not mesa:
        print("  Mesa inválida.")
        pausar()
        return

    itens_pedido = []

    while True:
        listar_estoque_breve()
        print("  Digite 0 para finalizar o pedido.\n")
        try:
            idx = int(input("  Número do item desejado: ")) - 1
        except ValueError:
            print("  Valor inválido.")
            continue

        if idx == -1:
            break

        if idx < 0 or idx >= len(estoque):
            print("  Item inválido.")
            continue

        try:
            qtd = float(input(f"  Quantidade de '{estoque[idx]['nome']}': "))
        except ValueError:
            print("  Valor inválido.")
            continue

        if qtd <= 0:
            print("  Quantidade deve ser positiva.")
            continue

        if qtd > estoque[idx]["quantidade"]:
            print(f"  Estoque insuficiente! Disponível: {estoque[idx]['quantidade']} {estoque[idx]['unidade']}.")
            continue


        estoque[idx]["quantidade"] -= qtd


        adicionado = False
        for ip in itens_pedido:
            if ip["nome"] == estoque[idx]["nome"]:
                ip["quantidade"] += qtd
                ip["subtotal"]   += qtd * estoque[idx]["preco"]
                adicionado = True
                break
        if not adicionado:
            itens_pedido.append({
                "nome":       estoque[idx]["nome"],
                "quantidade": qtd,
                "unidade":    estoque[idx]["unidade"],
                "preco_unit": estoque[idx]["preco"],
                "subtotal":   qtd * estoque[idx]["preco"],
            })

        print(f"  '{estoque[idx]['nome']}' adicionado ao pedido.")

    if not itens_pedido:
        print("  Nenhum item selecionado. Pedido cancelado.")
        pausar()
        return

    total = sum(ip["subtotal"] for ip in itens_pedido)
    pedido = {
        "id":     proximo_id,
        "mesa":   mesa,
        "itens":  itens_pedido,
        "total":  total,
        "status": "Aberto",
    }
    pedidos.append(pedido)
    proximo_id += 1
    salvar_dados()

    print(f"\n  Pedido #{pedido['id']} (Mesa {mesa}) criado! Total: R$ {total:.2f}")
    pausar()

def listar_pedidos():
    cabecalho("PEDIDOS REGISTRADOS")
    if not pedidos:
        print("  Nenhum pedido registrado.")
    else:
        print(f"  {'ID':<6} {'Mesa':<8} {'Status':<12} {'Total'}")
        separador()
        for p in pedidos:
            print(f"  #{p['id']:<5} {p['mesa']:<8} {p['status']:<12} R$ {p['total']:.2f}")
    pausar()

def ver_detalhes_pedido():
    listar_pedidos_breve()
    cabecalho("DETALHES DO PEDIDO")
    try:
        pid = int(input("  ID do pedido: "))
    except ValueError:
        print("  ID inválido.")
        pausar()
        return

    pedido = None
    for p in pedidos:
        if p["id"] == pid:
            pedido = p
            break

    if pedido is None:
        print("  Pedido não encontrado.")
        pausar()
        return

    print(f"\n  Pedido #{pedido['id']} | Mesa: {pedido['mesa']} | Status: {pedido['status']}")
    separador()
    print(f"  {'Item':<20} {'Qtd':<8} {'Un.':<6} {'Unit.':<10} {'Subtotal'}")
    separador()
    for ip in pedido["itens"]:
        print(f"  {ip['nome']:<20} {ip['quantidade']:<8} {ip['unidade']:<6} R$ {ip['preco_unit']:<8.2f} R$ {ip['subtotal']:.2f}")
    separador()
    print(f"  {'TOTAL:':<36} R$ {pedido['total']:.2f}")
    pausar()

def atualizar_status_pedido():
    listar_pedidos_breve()
    cabecalho("ATUALIZAR STATUS DO PEDIDO")
    try:
        pid = int(input("  ID do pedido: "))
    except ValueError:
        print("  ID inválido.")
        pausar()
        return

    pedido = None
    for p in pedidos:
        if p["id"] == pid:
            pedido = p
            break

    if pedido is None:
        print("  Pedido não encontrado.")
        pausar()
        return

    print("\n  Status disponíveis:")
    status_opcoes = ["Aberto", "Em preparo", "Pronto", "Entregue", "Cancelado"]
    for i, s in enumerate(status_opcoes):
        print(f"  {i+1}. {s}")

    try:
        opcao = int(input("\n  Escolha o novo status: ")) - 1
        if opcao < 0 or opcao >= len(status_opcoes):
            print("  Opção inválida.")
            pausar()
            return
    except ValueError:
        print("  Valor inválido.")
        pausar()
        return

    pedido["status"] = status_opcoes[opcao]
    salvar_dados()
    print(f"  Pedido #{pid} atualizado para '{pedido['status']}'.")
    pausar()

def listar_pedidos_breve():
    if not pedidos:
        return
    separador()
    print(f"  {'ID':<6} {'Mesa':<8} {'Status':<12} {'Total'}")
    separador()
    for p in pedidos:
        print(f"  #{p['id']:<5} {p['mesa']:<8} {p['status']:<12} R$ {p['total']:.2f}")
    separador()




def relatorio():
    cabecalho("RELATÓRIO GERAL")


    total_pedidos   = len(pedidos)
    pedidos_abertos = sum(1 for p in pedidos if p["status"] == "Aberto")
    pedidos_entregues = sum(1 for p in pedidos if p["status"] == "Entregue")
    receita_total   = sum(p["total"] for p in pedidos if p["status"] == "Entregue")

    print(f"  Total de pedidos registrados : {total_pedidos}")
    print(f"  Pedidos em aberto            : {pedidos_abertos}")
    print(f"  Pedidos entregues            : {pedidos_entregues}")
    print(f"  Receita (entregues)          : R$ {receita_total:.2f}")


    separador()
    baixo = [item for item in estoque if item["quantidade"] < 5]
    if baixo:
        print("  ATENÇÃO - Itens com estoque baixo (< 5):")
        for item in baixo:
            print(f"    - {item['nome']}: {item['quantidade']} {item['unidade']}")
    else:
        print("  Nenhum item com estoque crítico.")

    pausar()




def menu_estoque():
    while True:
        cabecalho("MENU - ESTOQUE")
        print("  1. Listar estoque")
        print("  2. Adicionar item")
        print("  3. Atualizar quantidade")
        print("  4. Remover item")
        print("  0. Voltar")
        separador()
        opcao = input("  Opção: ").strip()

        if opcao == "1":
            listar_estoque()
        elif opcao == "2":
            adicionar_item_estoque()
        elif opcao == "3":
            atualizar_estoque()
        elif opcao == "4":
            remover_item_estoque()
        elif opcao == "0":
            break
        else:
            print("  Opção inválida.")
            pausar()

def menu_pedidos():
    while True:
        cabecalho("MENU - PEDIDOS")
        print("  1. Novo pedido")
        print("  2. Listar pedidos")
        print("  3. Ver detalhes de um pedido")
        print("  4. Atualizar status do pedido")
        print("  0. Voltar")
        separador()
        opcao = input("  Opção: ").strip()

        if opcao == "1":
            novo_pedido()
        elif opcao == "2":
            listar_pedidos()
        elif opcao == "3":
            ver_detalhes_pedido()
        elif opcao == "4":
            atualizar_status_pedido()
        elif opcao == "0":
            break
        else:
            print("  Opção inválida.")
            pausar()

def menu_principal():
    while True:
        cabecalho("SISTEMA DE RESTAURANTE")
        print("  1. Estoque")
        print("  2. Pedidos")
        print("  3. Relatório geral")
        print("  0. Sair")
        separador()
        opcao = input("  Opção: ").strip()

        if opcao == "1":
            menu_estoque()
        elif opcao == "2":
            menu_pedidos()
        elif opcao == "3":
            relatorio()
        elif opcao == "0":
            print("\n  Encerrando o sistema. Até logo!")
            break
        else:
            print("  Opção inválida.")
            pausar()


if __name__ == "__main__":
    carregar_dados()
    menu_principal()
