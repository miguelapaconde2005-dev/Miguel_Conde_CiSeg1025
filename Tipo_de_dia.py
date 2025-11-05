dia = input("Digite um dia da semana: ").lower()

match dia:
    case "sábado" | "sabado" | "domingo":
        print("Fim de semana")
    case "segunda" | "terça" | "terca" | "quarta" | "quinta" | "sexta":
        print("Dia útil")
    case _:
        print("Dia inválido")
