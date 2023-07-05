import pytest

from logic.same_key_words import SynonymsKeyWords

def test_read_dataset():
    dataset_filepath = 'data/synonyms_food.txt'

    synonyms_food = SynonymsKeyWords(dataset_filepath)

    assert isinstance(synonyms_food.data, dict)
    for key, value in synonyms_food.data.items():
        assert isinstance(key, str)
        assert isinstance(value, list)
        for item in value:
            assert isinstance(item, str)


def test_to_lower_case():
    dataset_filepath = 'data/synonyms_food.txt'
    synonyms_food = SynonymsKeyWords(dataset_filepath)
    assert synonyms_food.to_lower_case("Hello") == "hello"

def test_find_synonym():
    dataset_filepath = 'data/synonyms_food.txt'
    synonyms_food = SynonymsKeyWords(dataset_filepath)
    assert synonyms_food.find_synonym("МЕОД") == "Мед"
    assert synonyms_food.find_synonym("Pringles") == "Картофельные чипсы"
    assert synonyms_food.find_synonym("Неизвестное слово") == "Слово не найдено"