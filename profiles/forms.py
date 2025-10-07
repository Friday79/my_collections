from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, accessibility attributes, and classes.
        Remove auto-generated labels and set autofocus on first field.
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        autocomplete_attrs = {
            'default_phone_number': 'tel',
            'default_postcode': 'postal-code',
            'default_town_or_city': 'address-level2',
            'default_street_address1': 'address-line1',
            'default_street_address2': 'address-line2',
            'default_county': 'address-level1',
            'default_country': 'country',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True

        for field_name, field in self.fields.items():
            if field_name != 'default_country':
                placeholder = placeholders.get(field_name, field_name.replace('_', ' ').title())
                if field.required:
                    placeholder = f'{placeholder} *'
                field.widget.attrs['placeholder'] = placeholder
            else:
                # Add accessibility attributes for select element
                field.widget.attrs.update({
                    'title': 'Select your default country',
                    'aria-label': 'Select your default country',
                })

            field.widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            field.label = False
