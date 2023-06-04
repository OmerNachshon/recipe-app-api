from django.test import SimpleTestCase
import app.feature as feature

class FeatureTest(SimpleTestCase):
    """Testing new feature example"""
    def test_feature1(self):
        res=feature.func(2)
        self.assertEqual(res,4)
