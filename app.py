'''21 - Faça um Programa para um caixa eletrônico.
O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.'''


def otimiza_saque():
    valor_do_saque = float(input('Valor do Saque: '))

    nota = [1, 5, 10, 50, 100]
    vezes_usadas = [0, 0, 0, 0, 0]
    resultado = {}

    if valor_do_saque < 10 or valor_do_saque > 600:
        print('Valor indisponivel para saque.')
    else:
        notas_de_100 = valor_do_saque / nota[4]
        print(f'Nota 100: {notas_de_100}')
        resto_de_100 = valor_do_saque % nota[4]

        if resto_de_100 != 0:
            notas_de_50 = resto_de_100 / nota[3]
            print(f'Notas 50: {notas_de_50}')
            resto_de_50 = resto_de_100 % nota[3]

            if resto_de_50 != 0:
                notas_de_10 = resto_de_50 / nota[2]
                print(f'Notas 10: {notas_de_10}')
                resto_de_10 = resto_de_50 % nota[2]

                if resto_de_10 != 0:
                    notas_de_5 = resto_de_10 / nota[1]
                    print(f'Notas 5: {notas_de_5}')
                    resto_de_5 = resto_de_10 % nota[1]

                    if resto_de_5 != 0:
                        notas_de_1 = resto_de_5 / nota[0]
                        print(f'Notas 1: {notas_de_1}')


otimiza_saque()

