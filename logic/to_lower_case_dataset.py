import json


# TODO При необходимости для оптимизации можно создать поиск по датасету с обратным индексом, что ускорить вычислительную сложность

class ToLowerSynonymsKeyWords():
    def __init__(self, dataset_filepath: str):
        self.dataset_filepath = dataset_filepath
        self.data = self.read_dataset()

    def read_dataset(self) -> dict:
        with open(self.dataset_filepath, 'r') as f:
            data = json.load(f)

        return data

    def to_lower_case(self, string: str) -> str:
        return string.lower()

    def rewrite_dataset_to_lowwer(self) -> str:
        for key, values in self.data.items():
            self.data[key] = [value.lower() for value in values]


    def save_data(self):
        with open(self.dataset_filepath, 'w') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    gen_synonyms = ToLowerSynonymsKeyWords('data/synonyms_food.txt')
    gen_synonyms.rewrite_dataset_to_lowwer()
    gen_synonyms.save_data()

