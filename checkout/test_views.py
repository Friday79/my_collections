from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from bag.contexts import bag_contents
from checkout.models import Order
from django_countries.fields import Country


class CheckoutViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.checkout_url = reverse ('checkout')
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.session = self.client.session
        self.session['bag'] = {'1': 2}  # Fake product ID & quantity
        self.session.save()

    def test_checkout_success_view(self):
        from checkout.models import Order

        order = Order.objects.create(
            full_name='John Doe',
            email='john@example.com',
            phone_number='12345678',
            country='US',
            postcode='12345',
            town_or_city='Testville',
            street_address1='123 Test St',
            street_address2='',
            county='Test County',
        )
        url = reverse('checkout_success', args=[order.order_number])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
        self.assertIn('order', response.context)

    