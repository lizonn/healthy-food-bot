import ast
import random

from logic.same_key_words import SynonymsKeyWords

class AlternativeKeyFood:
    def __init__(self, dataset_filepath: str,synonyms_key_words_path:str):
        self.dataset_filepath = dataset_filepath
        self.data = self.read_dataset()
        self.synonyms_key_words_path = 'data/synonyms_food.txt'

    def read_dataset(self):
        with open(self.dataset_filepath, 'r') as f:
            data_str = f.read()
            data = ast.literal_eval(data_str)
            for key in data:
                data[key] = list(data[key])
        return data

    def select_random_alternative(self, alternatives):
        return random.choice(alternatives)

    def _preprocessed_word_for_key(self,word):
        return word.lower().capitalize()

    def _preprocessed_word_for_synonyms(self,word):
        return word.lower()

    def form_message(self, alternative):
        questions = [
            "Может, вам понравится это: ",
            "Что вы думаете о такой альтернативе: ",
            "А как насчет этого варианта: ",
            "Возможно, вам стоит попробовать это: ",
            "",
        ]
        random_question = random.choice(questions)
        return f"{random_question}{alternative}?"

    def get_alternative_for_word(self, word):
        try:
            alternatives = self.data[word]
            selected_alternative = self.select_random_alternative(alternatives)
            return self.form_message(selected_alternative)
        except KeyError:
            return None

    def get_synonym_and_find_alternative(self, word):
        synonyms = SynonymsKeyWords(self.synonyms_key_words_path)
        synonym_word = synonyms.find_synonym(word)
        if synonym_word != "Слово не найдено":
            return self.get_alternative_for_word(synonym_word)
        else:
            return None

    def get_alternative(self, keyword):
        keyword_key = self._preprocessed_word_for_key(keyword)
        message = self.get_alternative_for_word(keyword_key)
        if message:
            return message
        keyword_synonyms = self._preprocessed_word_for_synonyms(keyword)
        message = self.get_synonym_and_find_alternative(keyword_synonyms)
        if message:
            return message
        return "Мне жаль, но я не нашел альтернативы для данного продукта. Может быть, вы попробуете что-то другое?"





if __name__ == '__main__':

    alt_food = AlternativeKeyFood(dataset_filepath='data/food.txt',
                                  synonyms_key_words_path='data/synonyms_food.txt')
    print(alt_food.get_alternative('берн'))
