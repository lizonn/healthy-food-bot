import json

# TODO При необходимости для оптимизации можно создать поиск по датасету с обратным индексом, что ускорить вычислительную сложность

class SynonymsKeyWords():
    def __init__(self,dataset_filepath:str):
        self.dataset_filepath = dataset_filepath
        self.data = self.read_dataset()

    def read_dataset(self) -> dict:
        with open(self.dataset_filepath, 'r') as f:
            data = json.load(f)

        return data

    def to_lower_case(self,string:str) -> str:
        return string.lower()

    def find_synonym(self,word:str) -> str:
        word = self.to_lower_case(word)
        for key, values in self.data.items():
            if word in values:
                return key
        return "Слово не найдено"




if __name__ == '__main__':

    word_to_find = 'Макдоналдс'
    gen_synonyms = SynonymsKeyWords('data/synonyms_food.txt')

    print(gen_synonyms.find_synonym(word_to_find))
