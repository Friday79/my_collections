from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import UserProfile
from checkout.models import Order


class ProfileViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.profile = UserProfile.objects.get(user=self.user)
        self.order = Order.objects.create(
            order_number='1234567890',
            full_name='Test User',
            email='test@example.com',
            phone_number='123456789',
            country='SE',
            postcode='12345',
            town_or_city='Stockholm',
            street_address1='Testgatan 1',
            original_bag='{}',
            stripe_pid='stripe123',
            user_profile=self.profile,
        )

    def test_profile_view_redirects_if_not_logged_in(self):
        """ Ensure users who aren't logged in are redirected """
        response = self.client.get(reverse('profile'))
        self.assertRedirects(response, f'/accounts/login/?next=/profile/')

    def test_profile_view_logged_in(self):
        """ Logged-in users can access their profile page """
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertContains(response, 'Profile')

    def test_profile_post_updates_data(self):
        """ Submitting profile form via POST updates data """
        self.client.login(username='testuser', password='testpass123')
        post_data = {
            'default_phone_number': '987654321',
            'default_street_address1': 'New Street 12',
            'default_street_address2': '',
            'default_town_or_city': 'Uppsala',
            'default_county': 'Uppsala County',
            'default_postcode': '54321',
            'default_country': 'SE'
        }
        response = self.client.post(reverse('profile'), post_data)
        self.assertEqual(response.status_code, 200)
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.default_phone_number, '987654321')
        self.assertContains(response, 'Profile updated successfully')

    def test_order_history_view(self):
        """ Order history displays past order info correctly """
        response = self.client.get(reverse('order_history', args=['1234567890']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
        self.assertContains(response, 'order number 1234567890')
        