from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import UserProfile


class UserProfileModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')

    def test_user_profile_created_on_user_creation(self):
        """ Test that a UserProfile is created automatically when a User is created """
        profile = UserProfile.objects.get(user=self.user)
        self.assertIsInstance(profile, UserProfile)
        self.assertEqual(profile.user.username, 'testuser')

    def test_user_profile_str_returns_username(self):
        """ Test the string representation of UserProfile """
        profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(str(profile), 'testuser')    

   