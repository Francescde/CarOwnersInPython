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
        response = self.client.get('/cars/' + str(snippet.id) + '.json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = response.json()
        self.assertEqual(res['color'], 213)

    def test_delate_car(self):
        """
        Ensure you candelete a car.
        """
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user.save()
        self.client.login(username='john', password='johnpassword')
        snippet = Car(color=213, brand="SeatTest", owner=user)
        snippet.save()
        count_car = Car.objects.count()
        self.assertEqual(User.objects.count(), 1)
        response = self.client.delete('/cars/' + str(snippet.id) + '.json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Car.objects.count(), count_car-1)

    def test_user_has_to_be_loged_in_to_create_car(self):
        data = {'color': 213, 'brand': 'seadTest'}
        response = self.client.post('/cars/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)



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



