#print("Welcome to the rollercoaster!")
#height = int(input("What is your height in cm? "))

#if height > 120:

saldo = int(input("¿Cuál es tu saldo? "))
retiro = int(input("¿Cuánto quieres retirar? "))

if retiro <= 0:
    print("Cantidad inválida")
elif retiro > saldo:
    print("Saldo insuficiente")
elif retiro == saldo:
    print("Retiraste todo tu dinero")
else:
    print(f"Retiro exitoso. Tu saldo restante es: {saldo - retiro}")



