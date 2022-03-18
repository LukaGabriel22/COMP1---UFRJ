def media3(n1,n2,n3):
    '''funcao que retorna a media de tres numeros inteiros, dados por n1,n2 e n3
        float, float, float -> float'''
    return (n1 + n2 + n3)/3 

  
def difmaiores(n1,n2,n3):
    '''funcao que retorna, dados os numeros n1,n2 e n3, a diferença do maior
        deles com a media. float, float, float -> float'''
    return max(n1,n2,n3) - media3(n1,n2,n3)

  
def somamin(n1,n2,n3):
    '''funcao que retorna, dados os numeros n1,n2 e n3, a soma do menos deles
        com a media. float, float, float -> float'''
    return min(n1,n2,n3) + media3(n1,n2,n3)

  
def delta(a,b,c):
    '''funcao que dado os parametros a,b,c calcula o delta de um polinomio de
        segundo grau. int, int, int - float'''
    return b**2 - 4*a*c

  
def deltasoma(a,b,c):
    '''funcao que retorna a soma entre o delta e uma primeira raiz
        de uma equacao de segundo grau, dado os coeficientes a,b,c
            float, float, float -> float'''
    return -b + math.sqrt(delta(a,b,c))/(2*a) + delta(a,b,c)

  
def deltasub(a,b,c):
    '''funcao que retorna a subtracao entre o delta e uma segunda raiz
        de uma equacao de segundo grau, dado os coeficientes a,b,c
            float, float, float -> float'''
    return - b + math.sqrt(delta(a,b,c))/(2*a) + delta(a,b,c)
        

def termos(vi,vf,r):
    '''funcao que calcula o numero de termos dado o valor inicial vi,
        valor final vf e razao r
            int,int,int -> int'''
    return (vf - vi)/r + 1
##b)
def somak(vi,vf,r):
    '''funcao que calcula a soma de uma progressao aritimetica, dado o
        valor inicial vi, o valor final vf e a razao r
                int, int, int, -> int'''
    return (vi + vf) * ntermos(vi,vf,r)/2



def pi():
    '''funcao que retorna o valor de pi, sendo 3.14
        Sem parâmetro de entrada -> float'''
    return 3.14
  
  
def abcil(r):
    '''funcao que retorna a area de base de um cilindro, tendo como parametros
       o  valor pi e o raio r;  float -> float'''
    return 2*pi()*(r**2)

  
def alcil(r,al):
    '''funcao que retorna a area lateral de um cilindro, dado os parametros
        o raio r e a altura al; float,float -> float'''
    return 2*pi()*r*al

  
def atcil(r,al):
    '''funcao que retorna a area total de um cilindro, dado os parametros
        raio r, altura al e usando as funcoes anteriores de area lateral
            e area de base; float, float -> float'''
    return 2* abcil(r)+ alcil(r,al)


def hipotenu(a,b):
    '''funcao que retorna o valor da hipotenusa de um triangulo retangulo
        dado os catetos a e b; float,float -> float'''
    return math.sqrt(a**2 + b**2)

  
def dispo(x1,y1,x2,y2):
    '''funcao que calcula a distancia entre dois pontos em uma plano dado suas
        coordenadas x1, y1, x2, y2; float,float,float,float -> float'''
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

  
def peritri(a,b):
    '''funcao que retorna o perimetro de um triangulo reto dado os catetos
        a e b, usando tambem a funcao da hipotenusa; float,float -> float '''
    return a + b + hipote(a,b)

  
def somsencos2(x):
    '''funcao que caulcua a soma do quadrado do seno e do quadrado do cossenos
        de um angulo x. int -> int  '''
    return (math.sin(math.radians(x))**2) + (math.cos(math.radians(x))**2)


def comcir(r):
    '''funcao que retorna o comprimento de um circulo, dado o raio e
        usando a funcao que retorna o valor de pi
        float -> float'''
    return 2*math.pi*r

  
def setcirc (r,ang=60):
    ''' funcao que retorna a area de um setor circular, dado seu raio e
        o angulo, com argumento default sendo igual a 360
            float -> float'''
    return ang * (3.14* r**2)/360
