def separarPalavras(texto):
    palavras = []
    palavra = ""
    sinais_pontuacao = {" ", ".", ",", "!", "?"}

    for caracter in texto:
        if caracter in sinais_pontuacao:
            if palavra:
                palavras.append(palavra)
                palavra = ""
        else:
            palavra += caracter

    if palavra:
        palavras.append(palavra)

    return palavras


def qntPalavras(texto):
    palavras = separarPalavras(texto)
    return len(palavras)


if __name__ == "__main__":
    texto = input("Texto:")
    print(qntPalavras(texto))
