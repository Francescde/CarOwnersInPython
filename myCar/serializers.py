from rest_framework import serializers
from django.contrib.auth.models import User
from myCar.models import Car


class CarSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Car
        fields = ('id', 'created', 'color', 'brand', 'owner')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email',)
        write_only_fields = ('password',)
        read_only_fields = ( 'is_superuser', 'is_active', 'date_joined',)