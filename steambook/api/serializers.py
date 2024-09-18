from rest_framework import serializers
from .models import User, Airticket


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username',)


class AirticketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Airticket
        fields = ('title', 'text', 'author', 'price', 'pub_date', )
        read_only_fields = ('author',)
