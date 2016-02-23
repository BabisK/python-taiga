from taiga.requestmaker import RequestMaker
import unittest
from mock import patch
from taiga import TaigaAPI
from taiga.models import Severity
from .tools import create_mock_json
from .tools import MockResponse


class TestProjectTemplates(unittest.TestCase):

    @patch('taiga.requestmaker.RequestMaker.get')
    def test_single_project_template_parsing(self, mock_requestmaker_get):
        mock_requestmaker_get.return_value = MockResponse(200, create_mock_json('tests/resources/project_template_details_success.json'))
        api = TaigaAPI(token='f4k3')
        project_template = api.project_templates.get(1)
        self.assertEqual(project_template.description, 'Sample description')
        self.assertEqual(len(project_template.roles), 6)
        self.assertTrue(isinstance(project_template.severities[0], Severity))