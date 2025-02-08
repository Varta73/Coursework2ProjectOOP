import os
import unittest

from src.vacancy import Vacancy

root_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(root_dir, "data")


class TestVacancy(unittest.TestCase):

    def test_vacancy_init(self):
        vacancy = Vacancy(
            vac_id=116763625,
            name="Middle Java Developer",
            city="Москва",
            url="http://example.com/vacancy/1",
            salary_from=0,
            salary_to=120000,
            currency="RUR",
            employment="Полная занятость",
            snippet="Заниматься разработкой на Python",
        )

        self.assertEqual(vacancy.name, "Middle Java Developer")
        self.assertEqual(vacancy.city, "Москва")
        self.assertEqual(vacancy.url, "http://example.com/vacancy/1")
        self.assertEqual(vacancy.salary_from, 0)
        self.assertEqual(vacancy.salary_to, 120000)
        self.assertEqual(vacancy.currency, "RUR")
        self.assertEqual(vacancy.employment, "Полная занятость")
        self.assertEqual(vacancy.snippet, "Заниматься разработкой на Python")

    def test_vacancy_srt(self):
        """Проверяет работу метода __str__."""
        vacancy = Vacancy(
            vac_id=116763625,
            name="Middle Java Developer",
            city="Москва",
            url="http://example.com/vacancy/1",
            salary_from=0,
            salary_to=120000,
            currency="RUR",
            employment="Полная занятость",
            snippet="Заниматься разработкой на Python",
        )
        expected_str = (
            "id: 116763625\n"
            "Название вакансии: Middle Java Developer\n"
            "Город: Москва\n"
            "Зарплата\nот: 0 RUR\nдо: 120000 RUR\n"
            "Тип занятости: Полная занятость\n"
            "Требования: Заниматься разработкой на Python\n"
            "Ссылка на вакансию: http://example.com/vacancy/1\n"
        )
        self.assertEqual(str(vacancy), expected_str)

    def test_add_vacancy(self, new_vacancy):
        test_vacancy = new_vacancy
