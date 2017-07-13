from __init__latest import TestController 
from pylons import url
from routes import url_for
from routes.util import URLGenerator


class TestCustomerController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='customer', action='index'))
       	assert response	
