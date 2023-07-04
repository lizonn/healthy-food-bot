import pytest

from logic.alternative_food import AlternativeFood


def test_read_data():
    dataset_filepath = 'data/food.txt'

    alt_food = AlternativeFood(dataset_filepath)

    assert isinstance(alt_food.data, dict)
    for key, value in alt_food.data.items():
        assert isinstance(key, str)
        assert isinstance(value, list)
        for item in value:
            assert isinstance(item, str)


def test_select_random_alternative():
    dataset_filepath = 'data/food.txt'
    alt_food = AlternativeFood(dataset_filepath)
    alternatives = ["alt1", "alt2", "alt3"]
    selected_alt = alt_food.select_random_alternative(alternatives)
    assert selected_alt in alternatives


def test_form_message():
    dataset_filepath = 'data/food.txt'
    alt_food = AlternativeFood(dataset_filepath)
    alternative = "alt1"
    message = alt_food.form_message(alternative)
    assert alternative in message
    assert message.endswith("?")


@pytest.mark.parametrize("keyword, expected_end", [
    ("Сахар", "?"),
    ("Unknown", "что-то другое?")
])
def test_get_alternative(keyword, expected_end):
    dataset_filepath = 'data/food.txt'
    alt_food = AlternativeFood(dataset_filepath)
    message = alt_food.get_alternative(keyword)
    assert message.endswith(expected_end)
