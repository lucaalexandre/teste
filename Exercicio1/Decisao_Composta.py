idade = int(input("Qual a sua idade do paciente? "))
doenca = input("O paciente tem uma doença infecciosa? ")

if idade >=65:
    print("Esse paciente tem prioridade")
    if doenca.lower() == "sim":
        print("O paciente tem uma doença infecciosa")
    else: print("O paciente não tem uma doença infecciosa")


elif idade < 64:
    print("Esse paciente não tem prioridade")
    if doenca.lower() == "sim":
        print("O paciente tem uma doença infecciosa")

    else: print("O paciente não tem uma doença infecciosa")



else: print("Não entendi a sua resposta")





