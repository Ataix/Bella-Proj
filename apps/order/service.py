from rest_framework import status
from rest_framework.response import Response

from apps.order.models import Order
from apps.order.serializers import OrderSerializer


class OrderCreateService:
    def create(self, request) -> Response:
        data = request.data
        serializer = OrderSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            if user:
                serializer.validated_data['customer_first_name'] = user.first_name
                serializer.validated_data['customer_last_name'] = user.last_name
                serializer.validated_data['customer_phone'] = user.phone
                order = Order.objects.create(**serializer.validated_data)
                return Response({'message': 'Created order with user'},
                                status=status.HTTP_201_CREATED)
            else:
                order = Order.objects.create(**serializer.validated_data)
                return Response({'message': 'Created order with no user'},
                                status=status.HTTP_201_CREATED)
