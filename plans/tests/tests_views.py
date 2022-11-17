from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from users.models import User

client = APIClient()
response_post = client.post('/api/plan/')
response_get = client.get('/api/plan/')
response_get = client.get('/api/plan/<pk>/')
response_patch = client.patch('/api/plan/<pk>/')
response_delete = client.delete('/api/plan/<pk>/')

class PlanViewTest(APITestCase):
    user = User.objects.create_user(email='superuser1@mail.com',username='superuser1',password='superuser',phone='9 1234 5678',first_name='super',last_name='user',birthdate='1996-04-17',is_superuser=True)
    token = Token.objects.create(user=user)
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

def test_if_login_superuser_return_token(self):
    response = self.client.post('/api/login/',{"email":"superuser1@mail.com","password":"superuser"})
    self.assertEqual(response.status_code, 200, {'token': self.token.key})

def test_if_costumer_can_create_a_plan(self):
    user = User.objects.create_user(email='costumer@mail.com',username='costumer',password='costumer',phone='9 1234 5678',first_name='cos',last_name='tumer',birthdate='1996-04-17',is_superuser=False)
    self.token = Token.objects.create(user=user)
    self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    response = self.client.post('/api/login/',{"email":"costumer@mail.com","password":"costumer"})

    response_post = client.post('/api/plan/', {"name":"Plano de ouro", "description": "Tem direito 1 ano de  academia", "tier": "Prata", "price": 800, "is_active": True})
    msg = f'Esperava o status_code {401} mas recebi {response_post.status_code}'
    self.assertEqual(response_post.status_code, 401, msg)

def test_if_can_create_a_plan(self):
    user = User.objects.create_user(email='superuser2@mail.com',username='superuser',password='superuser',phone='9 1234 5678',first_name='super',last_name='user',birthdate='1996-04-17',is_superuser=True)
    token = Token.objects.create(user=user)
    self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    response = self.client.post('/api/login/',{"email":"superuser2@mail.com","password":"superuser"})

    response_post = client.post('/api/plan/', {"name":"Plano de prata", "description": "Tem direito a 6 mês de academia", "tier": "Prata", "price": 400, "is_active": True})
    msg = f'Esperava o status_code {201} mas recebi {response_post.status_code}'
    self.assertEqual(response_post.status_code, 201, msg)
    
def test_if_can_create_a_plan_with_keys_wrongs(self):
    user = User.objects.create_user(email='superuser3@mail.com',username='superuser',password='superuser',phone='9 1234 5678',first_name='super',last_name='user',birthdate='1996-04-17',is_superuser=True)
    token = Token.objects.create(user=user)
    self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    response = self.client.post('/api/login/',{"email":"superuser3@mail.com","password":"superuser"})

    response_post = client.post('/api/plan/', {"username":"Plano de prata", "description": "Tem direito a 6 mês de academia", "tier": "Prata", "price": 400, "is_active": True})
    msg = f'Esperava o status_code {400} mas recebi {response_post.status_code}'
    self.assertEqual(response_post.status_code, 400, msg)

def test_if_can_list_a_plan(self):
    user = User.objects.create_user(email='superuser4@mail.com',username='superuser',password='superuser',phone='9 1234 5678',first_name='super',last_name='user',birthdate='1996-04-17',is_superuser=True)
    token = Token.objects.create(user=user)
    self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    response = self.client.post('/api/login/',{"email":"superuser4@mail.com","password":"superuser"})

    response_get = client.get('/api/plan/')
    msg = f'Esperava o status_code {200} mas recebi {response_get.status_code}'
    self.assertEqual(response_get.status_code, 200, msg)

def test_if_can_filter_a_plan(self):
    user = User.objects.create_user(email='superuser4@mail.com',username='superuser',password='superuser',phone='9 1234 5678',first_name='super',last_name='user',birthdate='1996-04-17',is_superuser=True)
    token = Token.objects.create(user=user)
    self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    self.response = self.client.post('/api/login/',{"email":"superuser4@mail.com","password":"superuser"})

    response_get = client.get(f'/api/plan/{self.response.post.id}/')
    msg = f'Esperava o status_code {200} mas recebi {response_get.status_code}'
    self.assertEqual(response_get.status_code, 200, msg)

def test_if_can_updated_a_plan(self):
    user = User.objects.create_user(email='superuser5@mail.com',username='superuser',password='superuser',phone='9 1234 5678',first_name='super',last_name='user',birthdate='1996-04-17',is_superuser=True)
    token = Token.objects.create(user=user)
    self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    self.response = self.client.post('/api/login/',{"email":"superuser5@mail.com","password":"superuser"})

    response_patch = client.patch(f'/api/plan/{self.response.post.id}/', {"description": "Tem direito a 1 semestre de academia"})
    msg = f'Esperava o status_code {200} mas recebi {response_patch.status_code}'
    self.assertEqual(response_patch.status_code, 200, msg)

def test_if_can_delete_a_plan(self):
    user = User.objects.create_user(email='superuser6@mail.com',username='superuser',password='superuser',phone='9 1234 5678',first_name='super',last_name='user',birthdate='1996-04-17',is_superuser=True)
    token = Token.objects.create(user=user)
    self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    self.response = self.client.post('/api/login/',{"email":"superuser6@mail.com","password":"superuser"})

    response_delete = client.delete(f'/api/plan/{self.response.post.id}/')
    msg = f'Esperava o status_code {204} mas recebi {response_delete.status_code}'
    self.assertEqual(response_delete.status_code, 204, msg)

def test_if_can_delete_a_plan_without_plan_id(self):
    user = User.objects.create_user(email='superuser7@mail.com',username='superuser',password='superuser',phone='9 1234 5678',first_name='super',last_name='user',birthdate='1996-04-17',is_superuser=True)
    token = Token.objects.create(user=user)
    self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    self.response = self.client.post('/api/login/',{"email":"superuser7@mail.com","password":"superuser"})

    response_delete = client.delete(f'/api/plan/pk/')
    msg = f'Esperava o status_code {400} mas recebi {response_delete.status_code}'
    self.assertEqual(response_delete.status_code, 400, msg)

