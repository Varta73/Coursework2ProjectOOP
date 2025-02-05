import unittest
from unittest.mock import patch, Mock
from src.vacancy_api import HHApi


class TestHHApi(unittest.TestCase):

    @patch("requests.get")
    def test_get_vacancies(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{'key': 'value'}]

        self.assertEqual(mock_get.return_value.status_code, 200)

    @patch("requests.get")
    def test_head_hunter_api_requests(self, test_requests_api):
        obj_api = HHApi()
        assert type(obj_api) is HHApi





