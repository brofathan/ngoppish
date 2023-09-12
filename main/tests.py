from django.test import TestCase, Client
from django.urls import resolve, reverse
from http import HTTPStatus

from .views import main_page
from main.models import Product

class main_test(TestCase):
    def test_main_url_is_exists(self):
        response = Client().get('/main/')
        self.assertEquals(response.status_code, HTTPStatus.OK)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    ################################################################

    def test_url_is_resolved(self):
        url = reverse("homepage")
        self.assertEquals(resolve(url).func, main_page)

    def test_product_name(self):
        self.product1 = Product.objects.create(name = "product1", amount = 1, description="description")

        self.assertEquals([self.product1.name, self.product1.amount, self.product1.description], 
                          ["product1", 1, "description"])