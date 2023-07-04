import ast
import random

class AlternativeFood:
    def __init__(self, dataset_filepath: str):
        self.dataset_filepath = dataset_filepath
        self.data = self.read_dataset()

    def read_dataset(self):
        with open(self.dataset_filepath, 'r') as f:
            data_str = f.read()
            # Преобразуем строку в словарь
            data = ast.literal_eval(data_str)
            # Преобразуем множества в списки
            for key in data:
                data[key] = list(data[key])
        return data

    def select_random_alternative(self, alternatives):
        return random.choice(alternatives)

    def form_message(self, alternative):
        questions = [
            "Может, вам понравится это: ",
            "Что вы думаете о такой альтернативе: ",
            "А как насчет этого варианта: ",
            "Возможно, вам стоит попробовать это: ",
        ]
        random_question = random.choice(questions)
        return f"{random_question}{alternative}?"

    def get_alternative(self, keyword):
        try:
            alternatives = self.data[keyword]
            selected_alternative = self.select_random_alternative(alternatives)
            return self.form_message(selected_alternative)
        except KeyError:
            return "Мне жаль, но я не нашел альтернативы для данного продукта. Может быть, вы попробуете что-то другое?"



if __name__ == '__main__':

    alt_food = AlternativeFood('data/food.txt')
    print(alt_food.get_alternative('Сахар'))
    print(alt_food.data.keys())
