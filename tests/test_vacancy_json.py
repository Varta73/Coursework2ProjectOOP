import os

from src.vacancy_json import JsonFile

root_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(root_dir, "data")


def test_write(test_add_vacancy):
    test_vacancy = test_add_vacancy

    json_saver = JsonFile(data_dir)
    json_saver.write(test_vacancy)

    # Ожидаемое содержимое файла
    test_read_file = (
        "id: 116763625\n"
        "Название вакансии: Middle Java Developer\n"
        "Город: Москва\n"
        "Зарплата\nот: 0 RUR\nдо: 120000 RUR\n"
        "Тип занятости: Полная занятость\n"
        "Требования: Заниматься разработкой на Python\n"
        "Ссылка на вакансию: http://example.com/vacancy/1\n"
    )

    with open(data_dir, encoding="utf-8") as file:
        assert test_read_file == file.read()
