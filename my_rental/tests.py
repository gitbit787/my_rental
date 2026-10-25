from django.test import SimpleTestCase

# Create your tests here.
class LoadMyRentalAppTest(SimpleTestCase):
    """
    Test cases for loading the MyRental application.
    Validates status codes and page title. The tests use SimpleTestCase 
    which is faster than TestCase for testing static pages.
    """
    def test_home_page_status_code(self):
        """
        Get the home page and verify it returns a 200 status code.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_contains_title(self):
        """
        Get the home page and verify the response contains the title "My Rental".
        """
        response = self.client.get('/')
        self.assertContains(response, 'My Rental')

    def test_home_page_not_found(self):
        """
        Get a non-existent page and verify it returns a 404 status code.
        """
        response = self.client.get('/nonexistent/')
        self.assertEqual(response.status_code, 404)
