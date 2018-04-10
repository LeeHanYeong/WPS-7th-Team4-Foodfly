from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import User

__all__ = (
    'UserSerializer',
    'EmailAuthTokenSerializer',
    'SignupSerializer',
)


class UserSerializer(serializers.ModelSerializer):
    phone_number = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'pk',
            'name',
            'phone_number',
            'email',
            'img_profile',
        )

    def get_phone_number(self, obj):
        return obj.phone_number.as_national


class EmailAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(username=email, password=password,
                                request=self.context.get('request'))
            if not user:
                raise serializers.ValidationError('자격인증정보가 올바르지 않습니다')
        else:
            raise serializers.ValidationError('이메일과 비밀번호를 입력해주세요')

        attrs['user'] = user
        return attrs


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'pk',
            'name',
            'phone_number',
            'email',
            'password',
            'password_confirm',
            'img_profile',
        )
        read_only_fields = (
            'pk',
        )

    def validate_email(self, value):
        if self.Meta.model.objects.filter(username=value).exists():
            raise serializers.ValidationError('해당 이메일은 이미 사용중입니다')
        return value

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError('비밀번호와 비밀번호 확인란의 입력값이 다릅니다')
        attrs.pop('password_confirm')
        return attrs

    def create(self, validated_data):
        return self.Meta.model.objects.create_email_user(**validated_data)

    def to_representation(self, instance):
        ret = {
            'user': UserSerializer(instance).data,
            'token': instance.token,
        }
        return ret
