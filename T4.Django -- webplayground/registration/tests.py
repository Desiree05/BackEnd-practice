from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='testuser', email="test@test.com", password='manolin12345')
        

    def test_profile_exists(self):
        exists = Profile.objects.filter(user__username='testuser').exists()
        self.assertEqual(exists, True)
        