from django.contrib.auth import get_user_model

from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.account.serializers import (
    RegisterSerializer, LoginSerializer, ProfileUserSerializer
)
from apps.account.service import (
    AccountCreateService, AccountLoginService, AccountLogoutService,
)
from apps.account.utils import IsOwnerAccount, UserViewSetMixin

ProfileUser = get_user_model()


class UserViewSet(UserViewSetMixin):
    queryset = ProfileUser.objects.all()
    serializer_class = ProfileUserSerializer
    permission_classes = [IsOwnerAccount]


class RegisterView(AccountCreateService, CreateAPIView):
    serializer_class = RegisterSerializer


class LoginView(AccountLoginService, GenericAPIView):
    serializer_class = LoginSerializer


class LogoutView(AccountLogoutService, GenericAPIView):
    permission_classes = [IsAuthenticated]
