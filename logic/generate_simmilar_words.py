import gensim


model_path = 'data/similar_words_model.bin/model.bin'


model = gensim.models.KeyedVectors.load_word2vec_format(model_path, binary=True)
similar_words = model.most_similar('чипсы_NOUN', topn=10)

for word, similarity in similar_words:
    print(word, similarity)

