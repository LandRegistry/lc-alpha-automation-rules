import pytest
from application.routes import app

reg_data = '{"keynumber": 222222, "ref": "myref", "date": "16/06/2015", "forename": "John", "surname": "Watson"}'


class TestAutomationRules:
    def setup_method(self, method):
        self.app = app.test_client()

    def test_healthcheck(self):
        response = self.app.get("/")
        assert response.status_code == 200

    def test_autocheck(self):
        headers = {'Content-Type': 'text'}
        response = self.app.post('/check_auto', data=reg_data, headers=headers)
        assert response.status_code == 200



