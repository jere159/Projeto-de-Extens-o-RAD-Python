# Importando a biblioteca necessária
import json

# Função para carregar dados dos pedidos
def carregar_pedidos(arquivo):
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Função para salvar dados dos pedidos
def salvar_pedidos(arquivo, pedidos):
    with open(arquivo, 'w') as f:
        json.dump(pedidos, f, indent=4)

# Função para adicionar um novo pedido
def adicionar_pedido(pedidos):
    nome_cliente = input("Nome do cliente: ")
    item = input("Item pedido: ")
    quantidade = int(input("Quantidade: "))
    pedido = {
        "nome_cliente": nome_cliente,
        "item": item,
        "quantidade": quantidade
    }
    pedidos.append(pedido)
    print("Pedido adicionado com sucesso!")

# Função para listar todos os pedidos
def listar_pedidos(pedidos):
    if not pedidos:
        print("Nenhum pedido encontrado.")
    else:
        for i, pedido in enumerate(pedidos):
            print(f"Pedido {i+1}:")
            print(f"  Nome do cliente: {pedido['nome_cliente']}")
            print(f"  Item pedido: {pedido['item']}")
            print(f"  Quantidade: {pedido['quantidade']}")
            print()

# Função principal
def main():
    arquivo = 'pedidos.json'
    pedidos = carregar_pedidos(arquivo)

    while True:
        print("1. Adicionar pedido")
        print("2. Listar pedidos")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_pedido(pedidos)
        elif escolha == '2':
            listar_pedidos(pedidos)
        elif escolha == '3':
            salvar_pedidos(arquivo, pedidos)
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
