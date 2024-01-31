from models.user import UserModel
from tests.base_test import BaseTest
import json


class UserTest(BaseTest):
    def test_register_user(self):
        with self.app() as c:
            with self.app_context():
                user_data = json.dumps({'username': 'test', 'password': '1234'})
                headers = {'Content-Type': 'application/json'}

                r = c.post('/register', data=user_data, headers=headers)

                self.assertEqual(r.status_code, 201)
                self.assertIsNotNone(UserModel.find_by_username('test'))
                self.assertDictEqual({'message': 'User created successfully.'},
                                     json.loads(r.data))

    def test_register_and_login(self):
        with self.app() as c:
            with self.app_context():
                user_data = json.dumps({'username': 'test', 'password': '1234'})
                headers = {'Content-Type': 'application/json'}

                c.post('/register', data=user_data, headers=headers)
                auth_response = c.post('/auth', data=user_data, headers=headers)

                self.assertEqual(auth_response.status_code, 200)
                self.assertIn('access_token', json.loads(auth_response.data).keys())

    def test_register_duplicate_user(self):
        with self.app() as c:
            with self.app_context():
                user_data = json.dumps({'username': 'test', 'password': '1234'})
                headers = {'Content-Type': 'application/json'}

                c.post('/register', data=user_data, headers=headers)
                r = c.post('/register', data=user_data, headers=headers)

                self.assertEqual(r.status_code, 400)
                self.assertDictEqual(d1={'message': 'A user with that username already exists'},
                                    d2=json.loads(r.data))
