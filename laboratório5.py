def criar_contato(nome,telefone="",email="",instagram=""):
    """Cria e retorna uma lista com as informações do contato(nome, telefone,
       email e instagram de um contato)e armazena esse contato em uma lista, apenas o nome é obrigatorio
       para criação do contato.
       str,str,str,str->list"""

    
    contato=[nome,[telefone],email,instagram]
    contatos=[]
    list.append(contatos,contato)
    return contatos
  
  
def atualizar_contato(info_contato,indice,informacao_nova):
    """Adiciona ou modifica uma informação de um contato existente.
       list,int,str->bool"""
    
    if indice!=1 and 0<=indice<=3:
        info_contato[indice]=informacao_nova
        return True
    elif indice==1 and 0<=indice<=3:
        if informacao_nova in info_contato[indice]:
            list.remove(info_contato[indice],informacao_nova)
            return True
        else:
            info_contato[indice]=info_contato[indice]+[informacao_nova]
            return True
    else:
        return False
      
      
def aminoacido(trincaRNA):
    """
        Dada uma trinca de RNA a função retorna a cadeia de aminoácidos corrspondente a proteína
        str -> str
        Parâmetros:
        Entrada: trincaRNA = uma trinca de RNA
        Retorna: uma cadeia de aminoaciodos que correponde a proteína da trinca de RNA
    """

    aminoacido = {'UUU':'Phe','CUU':'Leu','CUA':'Leu','AAG':'Lisina','UCU':'Ser','UAU':'Tyr','CAA':'Gln'}

    trinca1 = trincaRNA[:3]
    trinca2 = trincaRNA[3:6]
    trinca3 = trincaRNA[6:] 
    
    aminoacido1 = str(aminoacido[trinca1])
    aminoacido2 = str(aminoacido[trinca2])
    aminoacido3 = str(aminoacido[trinca3])
    
    return aminoacido1+'-'+aminoacido2+'-'+aminoacido3
