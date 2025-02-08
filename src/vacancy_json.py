import json
import os
from abc import ABC, abstractmethod

from src.vacancy import Vacancies, Vacancy

root_dir = os.path.dirname(__file__)
data_dir = os.path.join(root_dir, "data")


class BaseJsonFile(ABC):
    """Базовый класс для записи и чтения полученных вакансий в файл json"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def write(self, vacs: Vacancies):
        pass

    @abstractmethod
    def read_from_file(self):
        pass


class JsonFile(Vacancies, BaseJsonFile):
    """Запись и чтение json-файла"""

    def __init__(self, filename: str):
        super().__init__()
        self.__filename = filename
        self.__check_path_or_create()
        self.__filepath = os.path.join(data_dir, self.__filename)

    @staticmethod
    def __check_path_or_create() -> None:
        """Проверяет, существует ли папка, если нет то создает."""
        if not os.path.isdir(data_dir):
            os.makedirs(data_dir)

    def write(self, vacs: Vacancies):
        """Сохраняет список вакансий в json-файл."""
        with open(self.__filepath, "w", encoding="utf-8") as file:
            json.dump(vacs.to_list_dict(), file, indent=4, ensure_ascii=False)

    def read_from_file(self):
        """Загружает список вакансий из json-файла."""
        with open(self.__filepath, "r", encoding="UTF-8") as file:
            list_dict = json.load(file)
            self.__all_vacancies = []
            for vac in list_dict:
                self.__all_vacancies.append(Vacancy.to_list(vac))


def write_or_dont_write(vac_list: Vacancies) -> None:
    """Принимает список вакансий, и записывает его в json-файл."""

    print("Записать полученные данные в JSON файл?")
    user_answer = input("Да/Нет ").lower().strip()
    if user_answer != "да":
        print("Спасибо за использование программы!")
    else:
        jsonfile = JsonFile("vacancies.json")
        jsonfile.write(vac_list)
        print("Данные успешно записаны.\n")
