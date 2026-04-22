from django.test import TestCase, Client
from django.urls import reverse
from .core.services.inventory.test_service_inventory import InventoryServiceTest as InventoryServiceTest

class HomePageTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_homepageloading(self):
        response = self.client.get(reverse("home"))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/home/index.html")