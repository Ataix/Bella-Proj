from rest_framework.generics import (
    UpdateAPIView, DestroyAPIView, RetrieveAPIView
)
from rest_framework.permissions import BasePermission
from rest_framework.viewsets import ViewSetMixin


class IsOwnerAccount(BasePermission):
    """
    Determines whether the user has access to the account
    """
    def has_object_permission(self, request, view, obj) -> bool:
        return (obj.phone == request.user.phone or
                bool(request.user and request.user.is_superuser))


class UserViewSetMixin(ViewSetMixin,
                       RetrieveAPIView,
                       UpdateAPIView,
                       DestroyAPIView):
    pass
