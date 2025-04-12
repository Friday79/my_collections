import uuid
from django.test import TestCase
from django.conf import settings
from decimal import Decimal

from checkout.models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile
from django_countries.fields import Country
from django.contrib.auth.models import User


class OrderModelTests(TestCase):

    def setUp(self):
        # Create a test user and user profile
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.profile, created = UserProfile.objects.get_or_create(user=self.user)


        # Create a test product
        self.product = Product.objects.create(
            name='Test Product',
            description='A test product.',
            price=Decimal('50.00'),
            sku='TEST123'
        )

     # Create an order instance
        self.order = Order.objects.create(
            user_profile=self.profile,
            full_name='Test User',
            email='testuser@example.com',
            phone_number='1234567890',
            street_address1='123 Test St',
            town_or_city='Test City',
            country=Country('US'),
            postcode='12345',
            county='Test County',
            order_total=0,
            grand_total=0,
            stripe_pid='testpid',
        )

    def test_order_creation(self):
        """Test that the order number is generated correctly and the order can be saved"""
        self.assertTrue(self.order.order_number)
        self.assertEqual(len(self.order.order_number), 32)  # UUID length check
        self.order.save()
        self.assertIsNotNone(self.order.id)  # Ensure it has been saved to the database
    
    def test_update_total(self):
        """Test the `update_total` method"""
        order_line_item = OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=2,
        )
        self.order.update_total()
        self.assertEqual(self.order.order_total, 100.00)  # 2 products * $50
        self.assertEqual(self.order.grand_total, 100.00)  # No delivery cost if above threshold
