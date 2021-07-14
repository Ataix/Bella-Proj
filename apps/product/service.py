from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from apps.product.models import Wish


class WishListService(ListAPIView):
    def list(self, request, *args, **kwargs):
        """
        Overrides generic's ListAPIView's list function for customize queryset
        """
        queryset = self.filter_queryset(
            Wish.objects.filter(user=request.user)
        )
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
