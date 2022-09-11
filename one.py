agenda = {}

def chavescon(agenda, nome):
    chaves = []
    for chave in agenda:
        if chave.startswith(nome):
            chaves.append(chave)
    return chaves

def adicionar():
    Qtdcontatos = int(input('Quantos contatos deseja adicionar? '))
    while Qtdcontatos > 0:
        Nome = input("Digite o nome do contato:")
        Telefone = input("Digite o telefone do contato: ")
        agenda[Nome] = {
            'Nome': Nome,
            'Telefone': Telefone }           
        print('O contato {} foi cadastrado com sucesso!'.format(Nome))
        Qtdcontatos = Qtdcontatos - 1

def procurarcontato(nome, agenda):
    contatodebusca = []
    chaves1 = chavescon(agenda, nome)
    if len(chaves1) > 0:
        for chave in chaves1:
            contatodebusca.append([
                agenda[chave]["Nome"], agenda[chave]["Telefone"]
            ])
            print(contatodebusca)

def apagar(agenda, nome):
    if len(agenda) > 0:
      for contato in list(agenda):
        if contato == nome:
            agenda.pop(nome)
            print("O contato {} foi apagado da agenda!".format(nome))

def Editar(agenda, nome):
    if len(agenda) > 0:
        for chavdocontato in agenda:
            if chavdocontato == nome:
                novo_nome = input('Digite o novo nome do contato: ')
                novo_telefone = input('Digite o novo telefone do contato: ')
                agenda[novo_nome] = agenda.pop(nome)
                agenda[novo_nome] = {
                    "Nome": novo_nome,
                    "Telefone": novo_telefone                    
                }
                print("Os dados do contato {} foram alterados com sucesso!".format(nome))
                break

def relatorio(agenda):
    contatos = []
    if len(agenda) > 0:
        for chave in agenda:
            contatos.append([
                agenda[chave]["Nome"], agenda[chave]["Telefone"]
            ])
        print(contatos, headers=["Nome", "Telefone"], tablefmt="grid")
    else:
        print("Agenda vazia!")

def menu():
    while True:
        print('--> AGENDA TELEFONICA <--')
        print('1 - Adicionar contato')
        print('2 - Consultar contato')
        print('3 - Excluir contato')
        print('4 - Editar contato')
        print('5 - Sair')
        opc = int(input('Qual a opção desejada: ->'))

        if opc == 1:
            adicionar()
        elif opc == 2:
            nome = input('Digite o Nome que deseja buscar: ')
            procurarcontato(nome, agenda)
        elif opc == 3:
            nome = input('Digite o Nome do contato que deseja excluir: ')
            apagar(agenda, nome)
        elif opc == 4:
            nome = input('Digite o nome do contato que deseja alterar: ')
            Editar(agenda, nome)
    
        elif opc == 5:
            print('Agenda fechada!')
            break
        else:
            print('Opção invalida, selecione uma opção válida!')
menu()