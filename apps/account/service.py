from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from apps.account.serializers import RegisterSerializer

ProfileUser = get_user_model()


class AccountCreateService:

    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            phone = serializer.validated_data['phone']
            if phone:
                user = get_user_model().objects.all(phone=phone)
                user.create_activation_code()
                return Response(
                    {'message': "Created User with received phone"},
                    status=status.HTTP_201_CREATED
                )
            else:
                user = ProfileUser.objects.create_user(phone)
                user.create_activation_code()
                return Response({'message': "New User Created"},
                                status=status.HTTP_201_CREATED)


class AccountLoginService:

    def get(self, request, activation_code):
        user = get_object_or_404(ProfileUser, activation_code=activation_code)
        user.activation_code = ''
        user.save()
        return Response(
            'login successful',
            status=status.HTTP_200_OK
        )


class AccountLogoutService:

    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response('Successful logout')
