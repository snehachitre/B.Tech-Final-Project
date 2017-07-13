from __init__latest import TestController 
from pylons import url
from routes import url_for
from routes.util import URLGenerator

class TestJournalController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='journal', action='index'))
        assert response
