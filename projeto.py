num_inter = input('digite um numero inteiro: ')

if num_inter.isdigit():
    num_inter = int(num_inter)

    if num_inter % 2 == 0:
        print(f'{num_inter} é par')
    else:
        print(f'{num_inter} é impar')

else:
    print('isso nao e um numero intero')


hora = input('qual seu horario? ')

if hora.isdigit():
    hora = int (hora)

    if hora < 0 or hora > 23:
        print('horario deve estar entre 0 e 23')
    else:
        if hora <= 11:
            print('bom dia')
        elif hora <= 17:
            print('boa tarde')
        else:
            print('boa noite')
else:
    print('por favor, digite um horaio entre 0 e 23')
