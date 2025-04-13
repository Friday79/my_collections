from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product

class BagViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=10.00
        )
        self.bag_url = reverse('view_bag')
        self.add_url = reverse('add_to_bag', args=[self.product.id])
        self.adjust_url = reverse('adjust_bag', args=[self.product.id])
        self.remove_url = reverse('remove_from_bag', args=[self.product.id])

    def test_view_bag(self):
        response = self.client.get(self.bag_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_to_bag(self):
        response = self.client.post(self.add_url, {
            'quantity': 1,
            'redirect_url': self.bag_url
        })
        session = self.client.session
        bag = session.get('bag', {})
        self.assertIn(str(self.product.id), bag)
        self.assertEqual(bag[str(self.product.id)], 1)
        self.assertRedirects(response, self.bag_url)

    def test_adjust_bag(self):
        session = self.client.session
        session['bag'] = {str(self.product.id): 1}
        session.save()

        response = self.client.post(self.adjust_url, {
            'quantity': 2
        })
        session = self.client.session
        bag = session.get('bag', {})
        self.assertEqual(bag[str(self.product.id)], 2)
        self.assertRedirects(response, self.bag_url)

    def test_remove_from_bag(self):
        session = self.client.session
        session['bag'] = {str(self.product.id): 1}
        session.save()

        response = self.client.post(self.remove_url)
        self.assertEqual(response.status_code, 200)
        session = self.client.session
        bag = session.get('bag', {})
        self.assertNotIn(str(self.product.id), bag)
        