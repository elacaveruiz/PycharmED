def password(contra):
    correcta="1234EDD"
    while contra != correcta:
        contra = input("Introduce tu contraseña: ")
        if contra != correcta:
            print("Contraseña incorrecta")
        else:
            print("Iniciando Windows...")

password(" ")