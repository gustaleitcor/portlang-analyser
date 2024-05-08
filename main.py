from Analyser import Analyser

# odeio Rômulo portanto ele é ruim


def main():
    # Frase a ser analisada sintaticamente
    phrase = "Marcelo trabalha até 10 horas da noite"

    # Inicializando a gramática com a gramática do arquivo e frase alvo
    analyser = Analyser("grammar.mrg", phrase)
    # Analisa a frase alvo com a gramática
    b = analyser.analyse_phrase(phrase)

    # Se alguma árvore sintática for gerada
    if b == 0:
        print("Frase não reconhecida pela gramática.")
    # Se nenhuma árvore sintática for gerada
    else:
        print("Frase reconhecida pela gramática.")


if __name__ == "__main__":
    main()
