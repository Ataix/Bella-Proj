from rest_framework.permissions import BasePermission


class IsOwnerAccount(BasePermission):
    """
    Determines whether the user has access to the account
    """
    def has_object_permission(self, request, view, obj):
        return obj.phone == request.user.phone or \
               bool(request.user and request.user.is_superuser)
