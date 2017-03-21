from rest_framework import status
from rest_framework.test import APITestCase
from myCar.models import Car
from django.contrib.auth.models import User


class CarTests(APITestCase):
    def test_create_car(self):
        """
        Ensure we can create a new Car.
        """
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user.save()
        self.client.login(username='john', password='johnpassword')
        data = {'color': 213, 'brand': 'seadTest'}
        response = self.client.post('/cars/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Car.objects.count(), 1)
        self.assertEqual(Car.objects.get().brand, 'seadTest')

    def test_get_car(self):
        """
        Ensure you can get an snnipet.
        """
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user.save()
        snippet = Car(color=213,brand="SeatTest", owner=user)
        snippet.save()
        # TODO: preguntar per que aixo funciona
        response = self.client.get('/cars/' + str(snippet.id) + '.json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = response.json()
        self.assertEqual(res['color'], 213)

class UserTests(APITestCase):
    def test_create_user(self):
        """
        Ensure we can create a new User.
        """
        user = User.objects.create_superuser('john', 'lennon@thebeatles.com', 'johnpassword')
        user.save()
        self.assertEqual(User.objects.count(), 1)
        self.client.login(username='john', password='johnpassword')
        data = {"username":"franky","password":"thepassword"}
        response = self.client.post('/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)



