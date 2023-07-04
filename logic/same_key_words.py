import sys
import gensim, logging
import zipfile

import wget

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)



model_path = 'data/similar_words_model.bin/model.bin'


model = gensim.models.KeyedVectors.load_word2vec_format(model_path, binary=True)

def find_most_similar(word: str, words_list: list):
    most_similar = model.most_similar_to_given(word, words_list)
    return most_similar

words_list = ['сахар_NOUN', 'торт_NOUN', 'чипсы_NOUN', 'печенье_NOUN']

# Найдите наиболее подходящее слово из списка слов
most_similar_word = find_most_similar('картофель_NOUN', words_list)
print(most_similar_word)