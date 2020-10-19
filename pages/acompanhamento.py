import pages.projetosra

def acompanhar():
    user = int(input('Você é (1) cidadão ou (2) servidor?'))
    if (user == 1):
        int(input('Digite o número do recurso: '))
    elif(user == 2):
        projetosra.projetos()
    else:
        print("Opção inválida, tente novamente!")
        acompanhar()
        