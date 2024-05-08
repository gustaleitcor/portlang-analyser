from nltk import CFG
from nltk import draw
import nltk
from nltk.parse import ChartParser
import joblib
from nltk import word_tokenize

folder = 'trained_POS_taggers/'
teste_tagger = joblib.load(folder+'POS_tagger_brill.pkl')


class Analyser:
    def __init__(self, grammar_path: str, phrase: str):

        # Carrega a gramática do arquivo
        with open(grammar_path, 'r') as f:
            sintatic_grammar = f.read()

        word_grammar = ""
        # Tokeniza e analisa cada token lexicamente
        for word, type in teste_tagger.tag(word_tokenize(phrase)):

            # Se for pontuação, pula
            if type == word:
                continue

            # Efetua algumas correções do lexico
            type = type.replace("+", "_")
            word = word.replace("'", "`")
            if "|" in type:
                type = type.split("|")[0]

            # Garante que "da", "do", "na" e "no" sejam preposições
            if word in ["da", "do", "na", "no"]:
                # Incorpora à gramática caso a frase tenha alguma preposição
                word_grammar += f"PREP -> '{word}'\n"
                print(f"PREP -> '{word}'")
                continue

            # Incorpora à gramática o token analisado
            word_grammar += f"{type} -> '{word}'\n"
            print(f"{type} -> '{word}'")

        # Une a grmatica principal (arquivo) com a gramática dos tokens
        grammar = sintatic_grammar + word_grammar

        # Gera a gramática
        gramatica_cfg = CFG.fromstring(grammar)
        # Gera o parser
        self.parser = ChartParser(gramatica_cfg)

    def analyse_phrase(self, phrase: str):
        # Efetua alguma correções
        phrase = phrase.replace("'", "`")

        # Tokeniza a frase
        sentence = nltk.word_tokenize(phrase)
        # Analisa lexicamente a frase
        trees = self.parser.parse(sentence)

        # Gera a arvore sintática
        count = 0
        for tree in trees:
            if not tree:
                continue
            count += 1
            tree.pretty_print()  # printa a arvore sintática
            tree.draw()  # Mostra a arvore sintática

        return count
