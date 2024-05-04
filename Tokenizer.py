import joblib
import nltk


class Tokenizer:
    def __init__(self, folder):
        self.teste_tagger = joblib.load(folder+'POS_tagger_brill.pkl')

    def tokenize(self, phrase: str):
        word_tokens: list[str] = nltk.word_tokenize(phrase)
        return self.teste_tagger.tag(word_tokens)

    def normalize_tokens(self, tokens):
        phrase_norm: str = ""

        for token in tokens:
            phrase_norm += token[1] + " "

        # print(phrase_norm)

        return phrase_norm
