from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from apps.account.serializers import RegisterSerializer, LoginSerializer

ProfileUser = get_user_model()


class AccountCreateService:

    def get_response(self, request) -> Response:
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            phone = serializer.validated_data['phone']
            if phone:
                user = ProfileUser.objects.filter(phone=phone)
                return Response(
                    {'message': "Created User with received phone"},
                    status=status.HTTP_201_CREATED
                )
            else:
                user = ProfileUser.objects.create_user(phone)
                return Response({'message': "New User Created"},
                                status=status.HTTP_201_CREATED)


class AccountLoginService:

    def post(self, request) -> Response:
        data = request.data
        serializer = LoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            if not Token.objects.filter(user=user):
                Token.objects.create(user=user)
                return Response(
                    'login successful',
                    status=status.HTTP_200_OK
                )
            return Response(
                'token already issued',
                status=status.HTTP_200_OK
            )


class AccountLogoutService:

    def get(self, request) -> Response:
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response('Successful logout')
