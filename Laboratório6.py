def telefoneV(numero):
    '''A função verificará se um numero inserido corresponde a um numero de telefone
    válido no Brasil.
    Insira um numero entre aspas simples ou dupla com ou sem o DDD.
    A função retornará o DDD separado do telefone. Caso o número não seja
    válido, a função retornará uma tupla com duas strings vazias. Caso vocÊ
    não isira o DDD, o primeiro elemento da tupla será uma string vazia e o segundo
    com o numero inserido.
    OBS: Não é necessário colocar o DDI, pois a função apenas funcionará
    para número nos Brasil.
    Dado de entrada -> string
    Dado de saída -> tupla'''
    
    Q = len(numero) #Quantidade de caracteres

    #telefone com DDD
    if Q == 10:
        return (numero[0:2],numero[2:Q])
        
    #celular com DDD
    elif Q == 11 and numero[2] == "9":
        return (numero[0:2],numero[2:Q])

    #telefone sem DDD
    elif Q == 8:
        return (" ",numero)

    #celular sem DDD
    elif Q == 9 and numero[0] == "9":
        return (" ", numero)
    
    else:
        return (" ", " ")

def instagramV(insta):
    '''A função instagram possui o objetivo de verificar se a conta informada
    realmente pertence a uma conta do instagram.
    Dados de entrada -> string
    Dados de saída -> string'''

    Q = str.count(insta,'@')

    #Uma conta do instagram não pode ter espaço no meio e o primeiro caracter precisa ser sempre um '@'
    if Q == 1 and '@' in insta[0] and ' ' not in insta:
        return insta

    else:
        return ' '

def emailV(email):
    '''A função email possui o objetivo de verificar se um email informado
    é válido ou não.
    Dados de entrada -> string
    Dados de saída -> string'''

    Q = str.count(email,'@') #Um email só pode ter apenas um único '@'

    #Um email não pode ter o '@' nem no primeiro e nem no ultimo caracter. Além disso, não pode haver nenhum espaçamento entre os caracteres
    if Q == 1 and '@' in email[1:-1] and ' ' not in email:
        return email
    else:
        return ' '

def contatinhosApp_a(nome,telefone,email,instagram):
    '''A função contatinhosApp_a possui o objetivo de cadastrar um novo usuário
    na plataforma. Para realizar o cadastro, insira, em uma lista, respectivamente
    as seguintes informações: ['NOME',['TELEFONE'], 'EMAIL', 'INSTAGRAM' ]
    Dados de entrada -> string, string, string, string]
    Dados de saída -> lista[String, lista[string], string, string]'''

    tel = telefoneV(telefone)

    e_mail = emailV(email)

    insta = instagramV(instagram)

    return [nome, [tel], e_mail, insta]

def contatinhosApp_b(informacoes, i, nova):
    '''A função contatinhosApp_b possui o objetivo de atualizar algumas informações
    cadastradas anteriormente pelo usuário. Para isso, o usuário terá que inserior
    as informações atuais, o indice da informação que ele deseja atualizar e a informação nova.
    Dados de entrada -> lista[String, lista[string], string, string], int, string 
    Dados de saída -> lista[String, lista[string], string, string]'''

    nome = informacoes[0]
    
    email = informacoes[2]
    instagram = informacoes[3]

    Q_telefone = len(informacoes[1]) #Quantidade de telefones

    #Caso a atualização seja o nome
    if i == 0:
        informacoes[0] = nova


        return informacoes        

    #Caso a atualização seja do telefone
    if i == 1 and Q_telefone == 1:

        telefone = informacoes[1][0][0] + informacoes[1][0][1]
                       
        #Caso o telefone novo seja igual ao atual, a função removerá esse telefone
        if nova == telefone:

            del informacoes[1][0]

            return informacoes
                
        #Caso o telefone novo seja diferente do atual, a função adicionará esse novo telefone junto com o atual
        else:
            novaVerificada = telefoneV(nova)
            list.append(informacoes[1],novaVerificada)

            return informacoes

    #Situação em que o usuário iseriu dois telefone e deseja excluir 1
    elif i == 1 and Q_telefone == 2:

        telefone = informacoes[1][0][0] + informacoes[1][0][1]
        telefone2 = informacoes[1][Q_telefone - 1][0] + informacoes[1][Q_telefone - 1][1]

        #situação para excluir o segundo telefone
        if nova == telefone2:
            
            del informacoes[1][Q_telefone - 1]
            return informacoes

        #situação para excluir o primeiro telefone
        elif nova == telefone:
            
            del informacoes[1][0]
            return informacoes

        #situação em que o novo telefone informado é diferente dos dois inseridos
        else:
            novaVerificada = telefoneV(nova)
            list.append(informacoes[1],novaVerificada)

            return informacoes

    elif i == 1 and Q_telefone == 0:
        novaVerificada = telefoneV(nova)
        list.append(informacoes[1],novaVerificada)

        return informacoes
        

    #Caso a atualização seja do email
    elif i == 2:
        
        informacoes[2] = emailV(nova)


        return informacoes

    #Caso a atualização seja do instagram
    elif i == 3:

        informacoes[3] = instagramV(nova)

        return informacoes

    else:
        return informacoes
