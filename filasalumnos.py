def datosacomodados(data, datanomb):
    nombre =[]
    for i in datanomb:
        for c in i:
            nombre.append(c)
    arreglocorrecto = []
    arreglointerno =[]
    contador = 0
    contadornombre = 0
    for i in data:
        for c in i:
            if contador!=2 and contador!=3:
                if contador==1:
                    arreglointerno.append(nombre[contadornombre])
                else:
                    arreglointerno.append(c)
            contador+=1
        arreglocorrecto.append(arreglointerno)
        contadornombre+=1
        contador=0
        #arreglointerno.clear()
        
    return arreglocorrecto