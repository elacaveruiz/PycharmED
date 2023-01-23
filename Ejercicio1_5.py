def contador():
    frase = input("Introduce una frase: ")
    letra = input("Introduce una letra: ")
    contador = 0
    for letras in frase:
        if letras == letra:
            contador+=1
    print("La letra " + letra + ", aparece " + str(contador) + " veces en la frase: " + frase)
contador()