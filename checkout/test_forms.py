from django.test import TestCase
from .forms import OrderForm
from django_countries.fields import Country

class OrderFormTest(TestCase):

    def setUp(self):
        self.form_data = {
            'full_name': 'Test User',
            'email': 'testuser@example.com',
            'phone_number': '1234567890',
            'street_address1': '123 Test St',
            'street_address2': 'Apt 1',
            'town_or_city': 'Test City',
            'postcode': '12345',
            'country': 'US',
            'county': 'Test County',
        }
    
    def test_order_form_valid(self):
        """Test if the form is valid with correct data"""
        form = OrderForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_order_form_invalid(self):
        """Test if the form is invalid with missing required fields"""
        invalid_data = self.form_data.copy()
        invalid_data['email'] = ''
        form = OrderForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('This field is required.', form.errors['email'])    


