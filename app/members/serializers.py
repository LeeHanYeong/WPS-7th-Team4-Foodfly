from rest_framework import serializers

from .models import User

__all__ = (
    'UserSerializer',
    'SignupSerializer',
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'user_type',
            'email',
            'img_profile',
        )


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'pk',
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
            'user': super().to_representation(instance),
            'token': instance.token,
        }
        return ret
