saldo = float(input("Digite o saldo: "))
cheque = float(input("Digite o valor do cheque: "))

if cheque > saldo:
    print("Cheque não pode ser descontado!")
else:
    saldo -= cheque
    print(f"Cheque descontado, saldo: {saldo:.2f}€")
