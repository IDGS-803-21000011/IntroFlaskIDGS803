from io import open

archivo_texto = open('nombres.txt','r')

#archivo_texto.write('\n datos en el archivo')
#archivo_texto.close()

# print(archivo_texto.readline())
for lineas in archivo_texto.readlines():
    print(lineas.rstrip())

# archivo_texto.seek(10)

# print(archivo_texto.read())




archivo_texto.close()