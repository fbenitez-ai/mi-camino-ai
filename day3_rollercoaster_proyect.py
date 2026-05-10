#print("Welcome to the rollercoaster!")
#height = int(input("What is your height in cm? "))

if height >= 80:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age >= 12:
        bills = 5
        print("Child tickets are $5")
    elif age < 18:
        bills = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $7")

        wants_photo = input("Do you want to have a photo take? Type y for yes y n for no.")
        if wants_photo == "y":
            #Add 3 to their bill
    bill = bill + 3

else: print("Sorry you have to grow taller before you can ride")















#if height == 120:
#    print("Your can ride the roller coaster")
#else:
#    print("Sorry you have to grow taller before you can ride")



#saldo = int(input("¿Cuál es tu saldo? "))
#retiro = int(input("¿Cuánto quieres retirar? "))

#if retiro <= 0:
#   print("Cantidad inválida")
#elif retiro > saldo:
#   print("Saldo insuficiente")
#elif retiro == saldo:
#   print("Retiraste todo tu dinero")
#else:
    #print(f"Retiro exitoso. Tu saldo restante es: {saldo - retiro}")

#number_to_check = int(input("What is the number you want to check?"))
#if number_to_check % 2 == 0:
#    print("Even")
#else:
#    print("Odd")

