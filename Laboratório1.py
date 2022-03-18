def areaRetangulo (b, h):
    '''EX1:Insira as medidas da base (b) e da altura (h) em mesma unidade de comprimento
    p/ calcular a área do retângulo'''
    return b*h

def areaSuperficie (c):
    '''EX2:Insira a medida da aresta (c) p/ calcular a área da superfície de um cubo'''
    return c**2

def areaAnel (r1, r2):
    '''EX3:Insira as medidas (r1) e (r2)- na mesma unidade de comprimento -
    referentes aos dois raios da coroa circular (anel) formada por dois círculos p/
    calcular a área da mesma. Obs:(r1 > r2)'''
    return 3.14*(r1**2 - r2**2)

def media (x,y):
    '''EX4:Insira os valores de x e y para calcula a média aritmética desses dois números'''
    return (x+y)/2

def ordenadaSegundograu (a,b,c,x):
    '''EX5:Insira os parâmetros a, b, c e x de uma equação do segundo grau para calcular
    a ordenada dessa função (y),sendo o padrão da equação (y = ax² + bx +c)'''
    return (a*(x**2)) + (b*x) + c
    

def mediaPonderada (n1, p1, n2, p2):
    '''EX6:Calcula a média ponderada de dois numeros (n1 e n2)
    com seus respectivos pesos (p1 e p2)'''
    return ((n1*p1)+(n2*p2))/(p1+p2)

def erroPG (q, n):
    '''EX7:Calcula o erro (diferença) entre o valor da soma de uma PG infinita
    a partir de 1.0 (a1=1.0) e a soma dos n primeiros termos dessa PG, sendo
    0<= q < 1'''
    return (1 / (1 - q)) - (1*(q**n-1)/(1-q))

def gorjeta (v):
    '''EX8:Calcula o valor da gorjeta (10%) em cima do valor da conta do cliente (v)'''
    return v*.1

def gorjetaVariada (v, g):
    '''EX9:Insira o valor da conta do cliente (v) e a porcentagem da gorjeta (g)
    - apenas com números, como 10, 15, 5 - para obter o valor da gorjeta do garçom'''
    return v * g/100

def saldoFinal (si, m, t):
    '''EX10:Calcula o saldo final, dado o saldo inicial (si), o numero de meses (m)
    e a taxa de juros mensal (t), em porcentagem (formato:10)'''
    return si*(1+t*m/100)

def distCorrenteza (vc, lr, vb):
    '''EX11:Calcula a distância que a correnteza arrasta um barco que atravessa um rio.
    Insira a velocidade da correnteza (vc), a largura do rio (lr) e a velocidade do barco (vb)'''
    return (lr * 1.0/ vb) * vc
