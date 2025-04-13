from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from products.forms import ProductForm, ReviewForm
from products.models import Product, Category


class ProductFormTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='tech', friendly_name='Tech')

    def test_valid_product_form(self):
        form_data = {
            'name': 'Laptop',
            'description': 'High performance laptop.',
            'price': '999.99',
            'category': self.category.id,
            'has_sizes': False
        }
        form = ProductForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_product_form_missing_fields(self):
        form_data = {
            'name': '',
            'price': ''
        }
        form = ProductForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_product_form_has_custom_widget_class(self):
        form = ProductForm()
        for field_name, field in form.fields.items():
            self.assertIn('class', field.widget.attrs)
            self.assertIn('border-black', field.widget.attrs['class'])


class ReviewFormTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='books', friendly_name='Books')
        self.product = Product.objects.create(
            name='Novel',
            description='Interesting novel.',
            price=12.99,
            category=self.category
        )
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_valid_review_form(self):
        form_data = {
            'rating': 4,
            'comment': 'Loved it!',
        }
        form = ReviewForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_review_form_missing_data(self):
        form_data = {
            'comment': '',
        }
        form = ReviewForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_review_form_widgets(self):
        form = ReviewForm()
        self.assertEqual(form.fields['rating'].widget.__class__.__name__, 'Select')
        self.assertEqual(form.fields['comment'].widget.__class__.__name__, 'Textarea')
        