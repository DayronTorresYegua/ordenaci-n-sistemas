def algoritmoBurbuja(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def main():

    lista = [12, 5, 9, 1, 8]
    print(algoritmoBurbuja(lista))

if __name__ == '__main__':
    main()

