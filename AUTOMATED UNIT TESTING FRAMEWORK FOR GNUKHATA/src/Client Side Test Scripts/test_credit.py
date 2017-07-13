from __init__latest import TestController 
from pylons import url
from routes import url_for
from routes.util import URLGenerator


class TestCreditController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='credit', action='index'))
        assert response	
