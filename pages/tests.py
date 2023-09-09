from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class PageViewTest(TestCase):
    """Тест: Отображение страниц"""

    def test_home_url_exists_location(self):
        response = self.client.get(reverse('pages:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/index.html')
        self.assertContains(response, 'Edgecut')

