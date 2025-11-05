nota = int(input("Digite a nota (0-100): "))

match nota:
    case n if n >= 90:
        print("Excelente")
    case n if 70 <= n <= 89:
        print("Bom")
    case n if 50 <= n <= 69:
        print("Suficiente")
    case n if n < 50:
        print("Insuficiente")
