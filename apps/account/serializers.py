from django.contrib.auth import get_user_model

from rest_framework import serializers

ProfileUser = get_user_model()


class ProfileUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileUser
        fields = ('first_name', 'last_name', 'phone_number')


class LoginSerializer(serializers.Serializer):
    pass


class RegisterSerializer(serializers.ModelSerializer):
    pass
