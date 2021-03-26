from django.test import TestCase
from django.urls import reverse

from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='uma mensagem')
    
    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_text = f'{post.text}'
        self.assertEqual(expected_text, 'uma mensagem')


class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='teste view')
    
    def test_url_exists(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')