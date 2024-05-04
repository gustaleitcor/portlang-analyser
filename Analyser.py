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

        with open(grammar_path, 'r') as f:
            sintatic_grammar = f.read()

        word_grammar = ""
        for word, type in teste_tagger.tag(word_tokenize(phrase)):
            type = type.replace("+", "_")
            word = word.replace("'", "`")

            if type == word:
                continue

            if word in ["da", "do", "na", "no"]:
                word_grammar += f"PREP -> '{word}'\n"
                print(f"PREP -> '{word}'")
                continue

            if word in [".", ",", ":", ";", "!", "?", "..."]:
                word_grammar += f"PUNCT -> '{word}'\n"
                print(f"PUNCT -> '{word}'")
                continue

            if "|" in type:
                type = type.split("|")[0]

            word_grammar += f"{type} -> '{word}'\n"
            print(f"{type} -> '{word}'")

        grammar = sintatic_grammar + word_grammar

        gramatica_cfg = CFG.fromstring(grammar)
        self.parser = ChartParser(gramatica_cfg)

    def analyse_phrase(self, phrase: str):
        phrase = phrase.replace("'", "`")

        sentence = nltk.word_tokenize(phrase)
        trees = self.parser.parse(sentence)

        count = 0
        for tree in trees:
            if not tree:
                continue
            count += 1
            tree.pretty_print()
            tree.draw()

        return count
