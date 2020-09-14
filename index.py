import formulario
import naoprop


def sistemainicial():
    print('*****************************')
    print('Bem-vindo(a) ao sistema unificado da JARI')
    print('*****************************')

    print('O que você deseja fazer hoje?')
    opcaoservico = int(input('(1)Cadastrar recurso. (2)Acompanhar Recurso.'))

    if (opcaoservico == 1):
        print('*****************************')
        print('Você é o proprietário do veículo ou o condutor / infrator?')
        propInfr = int(input(print('(1)Sim (2)Não')))
        if (propInfr == 1):
            formulario.formulario()
        elif (propInfr == 2):
            naoprop.naoprop()
        else:
            print('Opção inválida')

    elif(opcaoservico == 2):
        print('Digite o número do recurso')
    else:
        print('Opção inválida')
