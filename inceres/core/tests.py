from django.test import TestCase

# Create your tests here.

class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/modulo_1/')

    def test_get(self):
        '''GET / must return status code 200'''

        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """
        Returns:must use index.html

        """
        self.assertTemplateUsed(self.response, 'hw1.html')