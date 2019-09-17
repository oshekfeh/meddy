from django.urls import reverse
from rest_framework.test import APITestCase
from . import views

# Create your tests here.
class APITests(APITestCase):
  def test_success_working_api(self):
    url = reverse('newsaggregator:list')
    response = self.client.get(url)
    assert response.status_code == 200
