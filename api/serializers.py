from api.models import User, Item
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer) :
    class Meta :
        model = User
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Item
        fields = '__all__'