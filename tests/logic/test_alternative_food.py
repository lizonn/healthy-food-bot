import pytest

from logic.alternative_food import AlternativeKeyFood


def test_read_data():
    dataset_filepath = 'data/food.txt'
    synonyms_key_words_path = 'data/synonyms_food.txt'

    alt_food = AlternativeKeyFood(dataset_filepath=dataset_filepath,
                                  synonyms_key_words_path=synonyms_key_words_path)

    assert isinstance(alt_food.data, dict)
    for key, value in alt_food.data.items():
        assert isinstance(key, str)
        assert isinstance(value, list)
        for item in value:
            assert isinstance(item, str)


def test_select_random_alternative():
    dataset_filepath = 'data/food.txt'
    synonyms_key_words_path = 'data/synonyms_food.txt'
    alt_food = AlternativeKeyFood(dataset_filepath=dataset_filepath,
                                  synonyms_key_words_path=synonyms_key_words_path)
    alternatives = ["alt1", "alt2", "alt3"]
    selected_alt = alt_food.select_random_alternative(alternatives)
    assert selected_alt in alternatives


def test_form_message():
    dataset_filepath = 'data/food.txt'
    synonyms_key_words_path = 'data/synonyms_food.txt'
    alt_food = AlternativeKeyFood(dataset_filepath=dataset_filepath,
                                  synonyms_key_words_path=synonyms_key_words_path)
    alternative = "alt1"
    message = alt_food.form_message(alternative)
    assert alternative in message
    assert message.endswith("?")

def test_get_alternative_for_word():
    dataset_filepath = 'data/food.txt'
    synonyms_key_words_path = 'data/synonyms_food.txt'
    alt_food = AlternativeKeyFood(dataset_filepath=dataset_filepath,
                                  synonyms_key_words_path=synonyms_key_words_path)
    word = 'Пиво'
    message = alt_food.get_alternative_for_word(word)
    assert message is not None

def test_get_alternative_for_word_not_found():
    dataset_filepath = 'data/food.txt'
    synonyms_key_words_path = 'data/synonyms_food.txt'
    alt_food = AlternativeKeyFood(dataset_filepath=dataset_filepath,
                                  synonyms_key_words_path=synonyms_key_words_path)
    word = 'Неизвестное слово'
    message = alt_food.get_alternative_for_word(word)
    assert message is None

def test_get_synonym_and_find_alternative():
    dataset_filepath = 'data/food.txt'
    synonyms_key_words_path = 'data/synonyms_food.txt'
    alt_food = AlternativeKeyFood(dataset_filepath=dataset_filepath,
                                  synonyms_key_words_path=synonyms_key_words_path)
    word = 'медд'
    message = alt_food.get_synonym_and_find_alternative(word)
    assert message is not None

def test_get_synonym_and_find_alternative_not_found():
    dataset_filepath = 'data/food.txt'
    synonyms_key_words_path = 'data/synonyms_food.txt'
    alt_food = AlternativeKeyFood(dataset_filepath=dataset_filepath,
                                  synonyms_key_words_path=synonyms_key_words_path)
    word = 'Неизвестное слово'
    message = alt_food.get_synonym_and_find_alternative(word)
    assert message is None

def test_get_alternative():
    dataset_filepath = 'data/food.txt'
    synonyms_key_words_path = 'data/synonyms_food.txt'
    alt_food = AlternativeKeyFood(dataset_filepath=dataset_filepath,
                                  synonyms_key_words_path=synonyms_key_words_path)
    keyword = 'Пиво'
    message = alt_food.get_alternative(keyword)
    assert message is not None

def test_get_alternative_synonym():
    dataset_filepath = 'data/food.txt'
    synonyms_key_words_path = 'data/synonyms_food.txt'
    alt_food = AlternativeKeyFood(dataset_filepath=dataset_filepath,
                                  synonyms_key_words_path=synonyms_key_words_path)
    keyword = 'медд'
    message = alt_food.get_alternative(keyword)
    assert message is not None

def test_get_alternative_not_found():
    dataset_filepath = 'data/food.txt'
    synonyms_key_words_path = 'data/synonyms_food.txt'
    alt_food = AlternativeKeyFood(dataset_filepath=dataset_filepath,
                                  synonyms_key_words_path=synonyms_key_words_path)
    keyword = 'Неизвестное слово'
    message = alt_food.get_alternative(keyword)
    assert message == "Мне жаль, но я не нашел альтернативы для данного продукта. Может быть, вы попробуете что-то другое?"

