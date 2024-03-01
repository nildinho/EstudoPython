print("Este Programa analisa os valores")
digito = input("Entre com o número de 0 a 6")


match digito:
    case '1' | '2':
        print("Segunda-feira, Você pode rodar")
    case '3' | '4':
        print("Terça-feira, Você não pode rodar")
    case '5' | '6':
        print("Quarta-feira, Você pode rodar ")
    case '7' | '8':
        print("Quinta-feira, Você não pode rodar")
    case '9' | '0':
        print("Sexta-feira, Você pode rodar ")