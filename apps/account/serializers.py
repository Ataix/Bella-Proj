from django.contrib.auth import get_user_model

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
            user = ProfileUser.objects.filter(phone=phone).first()
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
