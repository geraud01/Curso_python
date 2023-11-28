PALAVRAS_PROIBIDAS = ('Futebol', 'religião', 'politica')
textos = [
    'Joao gosta de futebol e politica',
    'A praia foi divertida'
]

for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print("Texto possui palavras proibidas:", palavra)
            break
    else:
        print("Texto autorizado:", texto)