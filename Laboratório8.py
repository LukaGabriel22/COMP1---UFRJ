#QUESTÃO 1
def elementos_iteravel(iteravel, elem):
	'''Conta quantas vezes um elemento aparece em iteravel
        iteravel, elemento -- > int'''
   soma = 0
	 for i in range(len(iteravel)):
       if elem == iteravel[i]:
          soma = soma + 1
          i+=1
  return soma

#QUESTÃO 2
def elementos_Rangeiteravel(iteravel, elem, ini, fim):
    '''A função recebe como parametro de entrada um iteravel, um elemento, um inteiro indicando o inicio do range e um inteiro indicando o fim.
        A função faz o mesmo processo de elementos_iteravel, mas agora dentro de um range espefico no iteravel, caso o elemento não for encontrado o contador retornara 0;
        iteravel, elemento, int,int --> int
    '''
    contador = 0
    for i in range(ini, fim):
        if iteravel[i] == elem:
            contador+=1

    return contador
  
#QUESTÃO 3
def mascara(palavra,lista,letra):
    '''jogo da forca'''
    '''str -> str'''
    elem=0

    for caractere in lista:
        if letra==caractere:
            return lista
    while elem < len(palavra):
        if letra in palavra[elem]:

            a = str.index(palavra,letra)
            list.insert(lista,a,letra)
            del lista [elem+1]
            
        elem += 1
        
    return lista
  
  
#QUESTÃO 4 - A
def soma_serie(n):
    '''Funcao que dado n, calcula a soma da série até o termo n
        int -> float'''
    soma = 0
    for i in range(n+1):
        soma = soma + ((-1)**i)/(2*i+1)
    return soma
  
  
#QUESTÃO 4 - B
def erro(erro=0.01):
   '''A função verificará quantos termos são necessários para que a soma de n termos da equação: ((-1)^n)/(2n + 1)
    possua um erro menor que 0.01 em relação a divisão (pi/4)
    None -> tupla(float,int)'''
    n = 0

    referencia = calculo(n)

    while math.fabs(1 - referencia) > erro:
        n = n + 1
        referencia = calculo(n)

    return (referencia,n)
