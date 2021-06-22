from django.contrib.auth import get_user_model, authenticate

from rest_framework import serializers

ProfileUser = get_user_model()


class ProfileUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileUser
        fields = (
            'first_name',
            'last_name',
            'phone'
        )


class RegisterSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(required=True)

    class Meta:
        model = ProfileUser
        fields = (
            'first_name',
            'last_name',
            'phone'
        )

    def validate_phone(self, value):
        if ProfileUser.objects.filter(phone=value).exists():
            raise serializers.ValidationError('phone is taken')
        return value


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(required=True)

    def validate(self, attrs):
        phone = attrs.get('phone')

        if phone:
            user = authenticate(
                request=self.context.get('request'),
                phone_number=phone
            )
            if not user:
                raise serializers.ValidationError(
                    "Can't login",
                    code='authorization'
                )
        else:
            raise serializers.ValidationError(
                'Write phone number'
            )
        attrs['user'] = user
        return attrs
