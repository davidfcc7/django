pesos = input('pesos colombianos: ')
pesos = float(pesos)
dolar = 3600

conversion = pesos / dolar
conversion = round(conversion, 2) #limitar la cantiad de decimales
conversion = str(conversion)

print('tienes $' + conversion + ' dolares')