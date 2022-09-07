from app.app import app

class TestApp:
    '''Flask application in flask_app.py'''

    def test_index_route(self):
        '''has a resource available at "/".'''
        response = app.test_client().get('/')
        assert(response.status_code == 200)

    def test_():
        pass
