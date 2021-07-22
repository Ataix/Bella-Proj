from rest_framework import permissions


class IsOwnerWish(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (obj.user == request.user or
                bool(request.user and request.user.is_superuser))


class ImageUrl:

    def _get_image_url(self, obj):
        request = self.context.get('request')
        image_obj = obj.images.first()
        if image_obj is not None and image_obj.image:
            url = image_obj.image.url
            if request is not None:
                url = request.build_absolute_uri(url)
            return url
        return ''
