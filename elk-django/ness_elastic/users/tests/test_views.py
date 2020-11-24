import pytest
from django.conf import settings
from django.test import RequestFactory
from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model
User = get_user_model()
import json

class RegisterUserTest(TestCase):

    email_pre_cadastrado = 'precadastradoemailteste128982@gmail.com'
    def setUp(self):
        
        User.objects.create(email=self.email_pre_cadastrado)
        self.client = Client()

   
    def testDifferentPasswords(self):
        response = self.client.post('/users/create/', {'name':'Nome Teste', 'password':'a23ja12u3hn', 'confirm_password':'a23j2u3hn',
                                                         'email':'emailteste123332118982@gmail.com'})

        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'success': False, 'message':'Os passwords são diferentes.'}
        )



    
