from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Category, Product, Review


class CategoryModelTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name='electronics',
            friendly_name='Electronics'
        )

    def test_str_method(self):
        self.assertEqual(str(self.category), 'electronics')

    def test_get_friendly_name(self):
        self.assertEqual(self.category.get_friendly_name(), 'Electronics')


class ProductModelTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name='books',
            friendly_name='Books'
        )
        self.product = Product.objects.create(
            category=self.category,
            sku='12345',
            name='Django for Beginners',
            description='A beginner-friendly Django guide.',
            has_sizes=False,
            price=29.99,
            rating=4.5,
            image_url='http://example.com/image.jpg'
        )

    def test_str_method(self):
        self.assertEqual(str(self.product), 'Django for Beginners')

    def test_product_category_relation(self):
        self.assertEqual(self.product.category.name, 'books')


class ReviewModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass')
        self.category = Category.objects.create(name='gadgets')
        self.product = Product.objects.create(
            name='Smartphone',
            description='Latest smartphone model.',
            price=499.99,
            category=self.category
        )
        self.review = Review.objects.create(
            product=self.product,
            user=self.user,
            rating=4,
            comment='Great product!'
        )

    def test_str_method(self):
        expected = f'Review by {self.user} for {self.product}'
        self.assertEqual(str(self.review), expected)

    def test_review_relationships(self):
        self.assertEqual(self.review.product, self.product)
        self.assertEqual(self.review.user, self.user)
        