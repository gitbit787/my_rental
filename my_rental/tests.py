from django.test import SimpleTestCase

# Create your tests here.
class LoadMyRentalAppTest(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_contains_title(self):
        response = self.client.get('/')
        self.assertContains(response, 'My Rental')

    def test_home_page_not_found(self):
        response = self.client.get('/nonexistent/')
        self.assertEqual(response.status_code, 404)
