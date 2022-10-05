num_int = input('digite um numero inteiro: ')

if num_int.isdigit():
    num_int = int(num_int)

    if num_int % 2 == 0:
        print(f'{num_int} é par')
    else:
        print(f'{num_int} é impar')

else:
    print('isso não e um numero inteiro')


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
    print('por favor, digite um horario entre 0 e 23')
