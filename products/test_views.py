from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Product, Category, Review
from django.core.files.uploadedfile import SimpleUploadedFile


class ProductViewsTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name='Test Category', friendly_name='Test Friendly')
        self.product = Product.objects.create(
            name='Test Product',
            description='Test description',
            price=10.00,
            category=self.category
        )
        self.superuser = User.objects.create_superuser(
            username='admin', password='adminpass', email='admin@test.com'
        )
        self.user = User.objects.create_user(username='user', password='userpass')

    def test_all_products_view(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertIn('products', response.context)

    def test_product_detail_view(self):
        url = reverse('product_detail', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_add_product_view_as_superuser(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_add_product_view_as_non_superuser(self):
        self.client.login(username='user', password='userpass')
        response = self.client.get(reverse('add_product'))
        self.assertRedirects(response, reverse('home'))

    def test_edit_product_view_as_superuser(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.get(reverse('edit_product', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product.html')

    def test_edit_product_view_as_non_superuser(self):
        self.client.login(username='user', password='userpass')
        response = self.client.get(reverse('edit_product', args=[self.product.id]))
        self.assertRedirects(response, reverse('home'))

    def test_delete_product_view_as_superuser(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.post(reverse('delete_product', args=[self.product.id]))
        self.assertRedirects(response, reverse('products'))
        self.assertFalse(Product.objects.filter(id=self.product.id).exists())

    def test_delete_product_view_as_non_superuser(self):
        self.client.login(username='user', password='userpass')
        response = self.client.post(reverse('delete_product', args=[self.product.id]))
        self.assertRedirects(response, reverse('home'))
        