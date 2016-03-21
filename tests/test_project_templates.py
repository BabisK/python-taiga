from taiga.requestmaker import RequestMaker
import unittest
from mock import patch
from taiga import TaigaAPI
from taiga.models import ProjectTemplate, ProjectTemplates
from taiga.models.base import InstanceResource
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
    
    @patch('taiga.requestmaker.RequestMaker.get')
    def test_list_project_templates_parsing(self, mock_requestmaker_get):
        mock_requestmaker_get.return_value = MockResponse(200, create_mock_json('tests/resources/project_template_list_success.json'))
        api = TaigaAPI(token='f4k3')
        project_templates = api.project_templates.list()
        self.assertEqual(project_templates[0].description, 'Sample description')
        self.assertEqual(len(project_templates), 1)
    
    @patch('taiga.models.base.ListResource._new_resource')
    def test_create_project_template(self, mock_new_resource):
        rm = RequestMaker('/api/v1', 'fakehost', 'faketoken')
        mock_new_resource.return_value = ProjectTemplate(rm)
        sv = ProjectTemplates(rm).create('PT 1', 'PT 1 slug', 'PT desc 1', 'product owner')
        mock_new_resource.assert_called_with(
            payload={'name': 'PT 1', 'slug': 'PT 1 slug', 'description': 'PT desc 1', 'default_owner_role': 'product owner',
                     'is_backlog_activated': False, 'is_kanban_activated': False, 'is_wiki_activated': False, 'is_issues_activated': False,
                     'us_statuses': '[]', 'points': '[]', 'task_statuses': '[]', 'issue_statuses': '[]', 'issue_types': '[]', 'priorities': '[]',
                     'severities': '[]', 'roles': '[]'}
        )
    
    @patch('taiga.requestmaker.RequestMaker.post')
    def test_add_us_status(self, mock_requestmaker_post):
        rm = RequestMaker('/api/v1', 'fakehost', 'faketoken')
        project_templates = Project_Template(rm, id=1)
        self.assertEqual(project.star().id, 1)
        mock_requestmaker_post.assert_called_with(
            '/{endpoint}/{id}/star',
            endpoint='projects', id=1
        )