from django.test import TestCase

class CrudTestViews(TestCase):

    def test_request_to_status_ok(self):
        response = self.client.get('/crud/')
        self.assertEqual(response.status_code,200)

    def test_create_new_user(self):
        response = self.client.post('/crud/users/',{'first_name':'OI','last_name':' Denovo','email':'test@test2.com','password':'123456781213'})
        self.assertEqual(response.status_code,201)

    def test_get_all_users(self):
        response = self.client.get('/crud/')
        self.assertEqual(response.status_code,200)
        self.assertJSONEqual(
            str(response.content, encoding='utf-8'),
            {'first_name':'Matheus','last_name':'Ramos','email':'test@test.com','password':'12345678'}
        )
