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
        
        
        



def calcular_puntos(dados, categoria):
    
    # GENERALA
    if categoria == "G":
        if dados.count(dados[0]) == 5:
            return 50
        else:
            return 0

    # POKER
    elif categoria == "P":
        for d in dados:
            if dados.count(d) >= 4:
                return 40
        return 0

    # FULL
    elif categoria == "F":
        valores = []
        for d in dados:
            if d not in valores:
                valores.append(d)

        if len(valores) == 2:
            if dados.count(valores[0]) == 3 and dados.count(valores[1]) == 2:
                return 30
            if dados.count(valores[1]) == 3 and dados.count(valores[0]) == 2:
                return 30
        return 0

    # ESCALERA
    elif categoria == "E":
        ordenados = sorted(dados)

        if ordenados == [1,2,3,4,5] or ordenados == [2,3,4,5,6]:
            return 20
        else:
            return 0

    # NUMEROS 1-6
    else:
        numero = int(categoria)
        puntos = dados.count(numero) * numero
        return puntos
    
    
dados = turno_jugador1()

print("Dados:", dados)

categoria = input("Elegí donde anotar (E, F, P, G o 1-6): ")

puntos = calcular_puntos(dados, categoria)

print("Sumaste", puntos, "puntos")