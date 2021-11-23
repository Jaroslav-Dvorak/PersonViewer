import json


class DB:
    def __init__(self):
        # self.persons = {"61b05a": "Jaroslav Dvořák", "111111": "Jméno Příjmení"}
        # with open("persons.json", "w", encoding='utf8') as f:
        #     json.dump(self.persons, f, ensure_ascii=False)

        with open("persons.json", "r", encoding='utf8') as f:
            self.persons = json.load(f)

    def read(self, hex_code):
        try:
            name = self.persons[hex_code]
        except KeyError:
            name = hex_code
        return name
