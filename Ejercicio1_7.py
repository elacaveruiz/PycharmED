def selector(lista_precios):
    lista_precios=[50, 75, 46, 80, 65, 8]
    precio_max=0
    precio_min=9999
    for precio in lista_precios:
        if precio > precio_max:
            precio_max=precio
        if precio < precio_min:
            precio_min=precio
    print("El mayor de los precios es: " + str(precio_max) + " y el menor de ellos es: " + str(precio_min))
selector("")