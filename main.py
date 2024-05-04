from Analyser import Analyser

# odeio Rômulo portanto ele é ruim


def main():
    phrase = "eu odeio Romulo e ele é ruim"

    # analyser = Analyser("grammar.mrg", "obj.json")
    analyser = Analyser("grammar.mrg", phrase)
    b = analyser.analyse_phrase(phrase)

    if b == 0:
        print("Frase não reconhecida pela gramática.")
    else:
        print("Frase reconhecida pela gramática.")


if __name__ == "__main__":
    main()
