import random


def tirar_dados(cantidad):
    dados = []
    for i in range(cantidad):
        dados.append(random.randint(1,6))
    return dados


def turno_jugador1():
    
    # PRIMERA TIRADA
    dados = tirar_dados(5)
    print("Primera tirada:", dados)

    tirada = 1

    while tirada < 3:

        decision = input("¿Querés volver a tirar dados? (s/n): ")

        if decision == "n":
            break

        print("Dados actuales:")
        for i in range(len(dados)):
            print(i+1, ":", dados[i])

        volver = input("Ingresá los números de los dados que querés volver a tirar separados por espacio (ej: 2 5): ")

        indices = volver.split()

        for i in indices:
            pos = int(i) - 1
            dados[pos] = random.randint(1,6)

        tirada += 1

        if tirada == 2:
            print("Segunda tirada:", dados)
        elif tirada == 3:
            print("Tercera tirada:", dados)

    print("Dados finales del turno:", dados)

    return dados
        
        
        

        
dado=turno_jugador1()
print(dado)