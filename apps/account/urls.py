from django.contrib.auth.views import LogoutView
from django.urls import path

from apps.account.views import RegisterView, LoginView, UserViewSet


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('profile/', UserViewSet.as_view({
        'get': 'retrieve',
        'patch': 'partial_update',
        'put': 'update'
    })),
]
