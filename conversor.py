menu = """
Bienvenido al conversor de monedas a Dolar 💲

1 - Peso Colombiano
2 - Peso Argentino
3 - Peso Mexicano

Escoja una opcion:  """

menu = int(input(menu))

if menu == 1:
    pesos = input('pesos colombianos: ')
    pesos = float(pesos)
    dolar = 3600

    conversion = pesos / dolar
    conversion = round(conversion, 2)  # limitar la cantiad de decimales
    conversion = str(conversion)

    print('tienes $' + conversion + ' dolares')

elif menu == 2:
    pesos = input('pesos Argentinos: ')
    pesos = float(pesos)
    dolar = 65

    conversion = pesos / dolar
    conversion = round(conversion, 2) #limitar la cantiad de decimales
    conversion = str(conversion)

    print('tienes $' + conversion + ' dolares')

elif menu == 3:
    pesos = input('pesos Mexicanos: ')
    pesos = float(pesos)
    dolar = 24

    conversion = pesos / dolar
    conversion = round(conversion, 2) #limitar la cantiad de decimales
    conversion = str(conversion)

    print('tienes $' + conversion + ' dolares')

else:
    print('escoja una opcion válida')
