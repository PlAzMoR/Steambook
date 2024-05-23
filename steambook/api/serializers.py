from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username',)


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'text', 'author', 'price', 'pub_date', )
        read_only_fields = ('author',)
