def dados():
  
    '''A função conta a quantidade de vezes que dois dados foram
    jogados até que os dois números desses dados foram iguais
    int'''

    dado1 = randint(1,6) 
    dado2 = randint(1,6)

    i = 1

    while dado1 != dado2:
        i = i + 1
        dado1 = randint(1,6) 
        dado2 = randint(1,6)
        
        
    return i



def buscar_contatos(lista, nome):
    '''A função retornará a posição dos nomes dentro de uma lista.
    lista - > string -> lista'''

    i = 0
    lista_nom = [] 
    Q = len(lista) 

    while i < Q:
        nomeinlista = str.lower(lista[i][0]) 

        if nome in nomeinlista:
            lista_nom = lista_nom + [i]

        i = i + 1

    return lista_nom
