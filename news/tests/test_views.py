from audioop import reverse
from unicodedata import category
from urllib import response
from django.test import TestCase

class ViewsTests(TestCase):
    
    def test_call_function_in_get_top_headlines(self):
        response = self.client.get('/news/')
        self.assertEqual(response.status_code,200)


    def test_call_search_news_editors(self):
        response = self.client.get('/news/search/editors/us/sports/en/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json()['status'],'ok')

    def test_call_search_news(self):
        response = self.client.get('/news/search/en/')
        self.assertEqual(response.status_code,200)
       
    def test_category_api_news(self):
        response = self.client.get('news/category/sports/')
        self.assertEqual(response.status_code,200)