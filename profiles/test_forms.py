from django.test import TestCase
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class UserProfileFormTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_user_profile_form_valid_data(self):
        form_data = {
            'default_phone_number': '1234567890',
            'default_postcode': '12345',
            'default_town_or_city': 'Uppsala',
            'default_street_address1': 'Main Street 1',
            'default_street_address2': 'Suite A',
            'default_county': 'Uppsala Län',
            'default_country': 'SE'
        }
        form = UserProfileForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_user_profile_form_widgets_have_placeholders_and_classes(self):
        form = UserProfileForm()
        expected_placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }
        for field in expected_placeholders:
            placeholder = form.fields[field].widget.attrs.get('placeholder', '')
            self.assertIn(expected_placeholders[field], placeholder)
            self.assertIn('profile-form-input', form.fields[field].widget.attrs.get('class', ''))

    def test_user_profile_form_labels_are_removed(self):
        form = UserProfileForm()
        for field in form.fields.values():
            self.assertFalse(field.label)
