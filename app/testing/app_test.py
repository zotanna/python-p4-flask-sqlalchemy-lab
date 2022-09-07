from app import app

class TestApp:
    '''Flask application in flask_app.py'''

    def test_animal_route(self):
        '''has a resource available at "/animal/<id>".'''
        response = app.test_client().get('/animal/1')
        assert(response.status_code == 200)

    def test_zookeeper_route(self):
        '''has a resource available at "/zookeeper/<id>".'''
        response = app.test_client().get('/zookeeper/1')
        assert(response.status_code == 200)

    def test_enclosure_route(self):
        '''has a resource available at "/enclosure/<id>".'''
        response = app.test_client().get('/enclosure/1')
        assert(response.status_code == 200)
