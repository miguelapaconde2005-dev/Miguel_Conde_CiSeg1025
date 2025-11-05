tipo = input("Digite o tipo de pedido (compra/venda): ").lower()
valor = float(input("Digite o valor do pedido: "))

pedido = {"tipo": tipo, "valor": valor}

match pedido:
    case {"tipo": "compra", "valor": v}:
        print(f"Compra de {v}€")
    case {"tipo": "venda", "valor": v}:
        print(f"Venda de {v}€")
    case _:
        print("Pedido desconhecido")
