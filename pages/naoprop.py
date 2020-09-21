import index


def naoprop():
    finalescolha = input(int(
        '(1) Finalizar sessão (2) Sou o proprietário do veículo ou o condutor / infrator '))
    if (finalescolha == 1):
        print('Obrigado, volte sempre!')
    elif (finalescolha == 2):
        index.sistemainicial()
    else:
        print('Opção inválida, sistema finalizado.')
