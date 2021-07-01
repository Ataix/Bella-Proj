from rest_framework.response import Response

from apps.order.models import Order


class OrderListService:
    def list(self, request, *args, **kwargs):
        order_queryset = Order.objects.filter(user=request.user)
        queryset = self.filter_queryset(order_queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
