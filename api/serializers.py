from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from api.models import Movie, Rating

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    #used to hash passwords
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'stars', 'user', 'movie', 'comments')


class MovieSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True)
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'no_of_ratings', 'avg_rating', 'ratings')
