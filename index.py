import pages.acompanhamento
import pages.formulario


def sistemainicial():
    print('*****************************')
    print('Bem-vindo(a) ao sistema unificado da JARI')
    print('*****************************')
    print('O que você deseja fazer hoje?')
    opcaoservico = int(input('(1)Cadastrar recurso. (2)Acompanhar Recurso.'))

    if (opcaoservico == 1):
        pages.formulario.formularios()
    elif(opcaoservico == 2):
        pages.acompanhamento.acompanhar()
    else:
        print('Opção inválida')
        sistemainicial()
