
frase_usuario = input("Ingrese una frase: ")

def extraer_vocales (frase_usuario):
    vocales = "aeiouAEIOU"
    vocales_frase = ""
    for caracter in frase_usuario:
        if caracter in vocales:
            vocales_frase += caracter
    return vocales_frase


def contar_vocales (vocales_en_frase):
    return len(vocales_en_frase)


vocales_en_frase = extraer_vocales(frase_usuario)

contador_vocales = contar_vocales(vocales_en_frase)

print (vocales_en_frase)
print (contador_vocales)
