segundos = int(input("Escreva o tempo em segundos: "))

horas = segundos // 3600
segundos %= 3600
minutos = segundos // 60
segundos %= 60

print(f"{horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s)")
