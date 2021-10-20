from flask_testing import TestCase
from artplatform import create_app
from artplatform.database import database as db
import unittest


class MyTest(TestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):
        return create_app('test')

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class SomeTest(MyTest):

    def test_index(self):
        response = self.client.get("/")
        self.assert200(response, "index page can not be displayed")

    def test_login(self):
        response = self.client.get("/login")
        self.assert200(response, "login page can not be displayed")

    def test_register(self):
        response = self.client.get("/register")
        self.assert200(response, "login page can not be displayed")


if __name__ == '__main__':
    unittest.main()
