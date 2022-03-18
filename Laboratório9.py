#QUESTÃO 1
def p_matriz(matriz,n):
    '''A função calculará o produto de duas matrizes.
    list -> float -> list'''

    inlinha = len(matriz)
    incoluna = len(matriz[0])
    resultado = []

    for i in range(inlinha):
        produto = []
        for j in matriz[i]:
            p = n * j
            list.append(produto,p)
        list.append(resultado,produto)
            
    return resultado
  
  #QUESTÃO 2
  def deumatch(afinidade):
    afinidades = []
    pessoas = afinidade.keys()
    for pessoa in pessoas:
        if pessoa == afinidade[afinidade[pessoa]]:
            afinidades.append((pessoa, afinidade[pessoa]))

    return afinidades
  
  
#QUESTÃO 3
def quem_ligou(lista, telefone):
    """
    Verifica nos dados de um usuário se um dado telefone existe nesta lista. Cas    o exista, retorna uma lista
    com os dados deste usuário e se não encontrar, devolve uma lista vazia.
    :list -> list
    :str -> str
    :list -> list
    """
    contatos = []
    for l in range(0, len(lista)):
	    for tel in range(0, len(lista[l])):
		    if telefone in lista[l] and telefone != '':
			    contatos.append(lista[tel])
		return contatos
  
  
