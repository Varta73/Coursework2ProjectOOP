import pytest

from src.vacancy import Vacancy


@pytest.fixture
def test_add_vacancy():
    return Vacancy(
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


@pytest.fixture
def test_read_file(self):
    return (
        f"id: {self.id}\n"
        f"Название вакансии: {self.name}\n"
        f"Город: {self.city}\n"
        f"Зарплата\nот: {self.salary_from} {self.currency}\nдо: {self.salary_to} {self.currency}\n"
        f"Тип занятости: {self.employment}\n"
        f"Требования: {self.snippet}\n"
        f"Ссылка на вакансию: {self.url}\n"
    )


@pytest.fixture
def test_requests_api():
    return [
        {
            "id": "116712519",
            "name": "Гувернантка (гувернер)",
            "city": "Москва",
            "salary_from": 200000,
            "salary_to": 200000,
            "currency": "RUR",
            "employment": "Полная занятость",
            "snippet": "Своевременное приучение к самостоятельности / навыки."
                       " ⁠инициативная / позитивная. ⁠ ⁠пунктуальная / заботливая.",
            "url": "https://hh.ru/vacancy/116712519",
        },
        {
            "id": "116763625",
            "name": "Middle Java Developer",
            "city": "Санкт-Петербург",
            "salary_from": 200000,
            "salary_to": 250000,
            "currency": "RUR",
            "employment": "Полная занятость",
            "snippet": "Оконченное высшее техническое образование. "
                       "Опыт работы на Java от 3-х лет. "
                       "Знание основ CS: алгоритмы, структуры данных, оценка сложности. ",
            "url": "https://hh.ru/vacancy/116763625",
        },
        {
            "id": "116790932",
            "name": "English teacher",
            "city": "Москва",
            "salary_from": 110000,
            "salary_to": 0,
            "currency": "RUR",
            "employment": "Полная занятость",
            "snippet": "Academic American or British pronunciation. "
                       "Experience of teaching preschool children, teaching groups "
                       "(at least 3 years of working experience). ",
            "url": "https://hh.ru/vacancy/116790932",
        },
        {
            "id": "115922174",
            "name": "Ассистент учителя школы",
            "city": "Москва",
            "salary_from": 110000,
            "salary_to": 0,
            "currency": "RUR",
            "employment": "Полная занятость",
            "snippet": "Высшее педагогическое образование. "
                       "Опыт работы в школе от 3 лет. "
                       "Уважительное и заботливое отношение ко всем участникам педагогического процесса.",
            "url": "https://hh.ru/vacancy/115922174",
        },
        {
            "id": "115113161",
            "name": "Управляющий делами семьи акционера (UHNWI)",
            "city": "Москва",
            "salary_from": 800000,
            "salary_to": 0,
            "currency": "RUR",
            "employment": "Полная занятость",
            "snippet": "Аналогичный опыт поддержки руководителя (акционер, собственник бизнеса) от 3х лет обязателен. "
                       "Высшее образование. Английский - advanced. Готовность к командировкам и...",
            "url": "https://hh.ru/vacancy/115113161",
        },
        {
            "id": "115446519",
            "name": "Системный администратор",
            "city": "Москва",
            "salary_from": 400000,
            "salary_to": 450000,
            "currency": "RUR",
            "employment": "Полная занятость",
            "snippet": "Практический опыт сопровождения распределенной "
                       "сетевой инфраструктуры на основе оборудования Cisco. "
                       "Уверенные знания и опыт работы с оборудованием Cisco на уровне...",
            "url": "https://hh.ru/vacancy/115446519",
        },
        {
            "id": "116709612",
            "name": "Учитель английского языка",
            "city": "Москва",
            "salary_from": 120000,
            "salary_to": 150000,
            "currency": "RUR",
            "employment": "Полная занятость",
            "snippet": "2) Уровень владения английским - не ниже С1. "
                       "3) Опыт работы <highlighttext>преподавателем</highlighttext> "
                       "английского в группах младших школьников - не менее 2...",
            "url": "https://hh.ru/vacancy/116709612",
        },
        {
            "id": "115703220",
            "name": "Администратор в школу",
            "city": "Москва",
            "salary_from": 120000,
            "salary_to": 0,
            "currency": "RUR",
            "employment": "Полная занятость",
            "snippet": "Требования: Опыт работы в административной сфере желателен. "
                       "Опыт работы с детьми будет преимуществом. "
                       "Уверенный пользователь ПК и оргтехники, знание MS...",
            "url": "https://hh.ru/vacancy/115703220",
        },
    ]
