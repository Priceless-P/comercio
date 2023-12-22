"""Unit tests for routes.py"""
import unittest
from application.models import Product
from application import create_app, db


class TestProductAPI(unittest.TestCase):
    """TestProduct class"""
    def setUp(self):
        """Setup method"""
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        """Tear down method"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_all_product(self):
        """Test GET /api/products route"""
        with self.app.app_context():
            response = self.client.get('/api/products')
            self.assertEqual(response.status_code, 200)

    def test_create_product(self):
        """Test POST /api/product/create route"""

        product = {
            'name': 'New test product',
            'price': 180,
            'slug': 'new-test-product',
        }

        response = self.client.post('/api/product/create', data=product)
        self.assertEqual(response.status_code, 200)

        created_product = Product.query.filter_by(slug='new-test-product').first()
        self.assertIsNotNone(created_product)
        self.assertEqual(created_product.name, 'New test product')

    def test_get_specfic_product(self):
        """Test GET /api/product/<slug> route"""
        with self.app.app_context():
            product = Product(name='Test product', price=78, slug='test_product')
            db.session.add(product)
            db.session.commit

            response = self.client.get('/api/product/{}'.format(product.slug))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['result']['name'], 'Test product')

    def test_delete_product(self):
        """Test DELETE /api/product/delete/<slug> route"""
        product = Product(name='Test Product', price=10.0, slug='test-product')
        db.session.add(product)
        db.session.commit()

        response = self.client.post('/api/product/delete/{}'.format(product.slug))
        self.assertEqual(response.status_code, 200)

        deleted_product = Product.query.filter_by(slug=product.slug).first()
        self.assertIsNone(deleted_product)
