def main ():
    
    valor1 = int(input("Digite um valor: "))
    valor2 = int(input("Digite outro valor: "))

    soma = valor1 + valor2
    sub = valor1 - valor2
    mult = valor1 * valor2
    div = valor1 / valor2

    print("-="*15)
    print(f"A soma é {soma}")
    print(f"A subtração é {sub}")
    print(f"A multiplicação é {mult}")
    print(f"A divisão é {div:.2f}")
    print("-="*15)

    continuar = int(input("Deseja continuar? \n1. Sim \n2. Sair\n" ))
    if continuar == 1:
        main()

    else:
        print("Saindo...")
        exit()

if __name__ == "__main__":
    main()