from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    
    def test_create_user_with_email_successfull(self):
        """ Test Creating a new user with email is successfull """
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_with_email_normalized(self):
         """ Test the email for new user is normalized """
         email = 'test@example.com'
         user = get_user_model().objects.create_user(email,'test123')

         self.assertEqual(user.email,email.lower())

    # def test_new_user_invalid_email(self):
    #     """ Test creating user with no email raise error """
    #     with self.assertRaises(ValueError):
    #         get_user_model().objects.create_user(Name,'test123')

    def test_create_new_superuser(self):
        """ Test creating a new superuser """
        user = get_user_model().objects.create_superuser(
            'test.demo@g.com',
            'test123'
        )        
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
