file = open(r'expeditionData.txt', 'r')
c68 = 0
 
for line in file:
    seis = False
 
    for digit in line:
 
        if digit == '6':
            seis = True
           
        if digit == '8' and seis:
            c68 = c68 + 1
            break
 
file.close()
print(f'La cantidad de veces que 68 estuvo en el archivo fue de {c68}')
 
