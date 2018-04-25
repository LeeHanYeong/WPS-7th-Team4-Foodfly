from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import APIException
from rest_framework.generics import get_object_or_404

from members.serializers import UserSerializer
from ..serializers import OrderSerializer
from ..models import OrderReview, OrderReviewImage, Order

__all__ = (
    'OrderReviewSerializer',
    'OrderReviewCreateSerializer',
    'OrderReviewUpdateSerializer',
)


class OrderReviewImageSerializer(serializers.ModelSerializer):
    origin = serializers.ImageField(source='image', read_only=True)

    class Meta:
        model = OrderReviewImage
        fields = (
            'pk',
            'origin',
        )


class OrderReviewSerializer(serializers.ModelSerializer):
    images = OrderReviewImageSerializer(many=True)
    user = UserSerializer()
    order = OrderSerializer()

    class Meta:
        model = OrderReview
        fields = (
            'pk',
            'user',
            'order',
            'score',
            'comment',
            'images',
        )


class OrderReviewCreateSerializer(serializers.ModelSerializer):
    orderPk = serializers.IntegerField()
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        write_only=True,
    )
    images = serializers.ListField(
        child=serializers.ImageField()
    )

    class Meta:
        model = OrderReview
        fields = (
            'pk',
            'orderPk',
            'user',
            'score',
            'comment',
            'images',
        )

    def validate_orderPk(self, pk):
        order = get_object_or_404(Order, pk=pk)
        if order.user != self.context['user']:
            raise APIException('주문자가 아닙니다')
        return pk

    def create(self, validated_data):
        images = validated_data.pop('images')
        order = get_object_or_404(Order, pk=validated_data.pop('orderPk'))
        validated_data['order'] = order
        with transaction.atomic():
            review = super().create(validated_data)
            for image in images:
                review.images.create(image=image)
        return review

    def to_representation(self, instance):
        return OrderReviewSerializer(instance).data


class OrderReviewUpdateSerializer(serializers.ModelSerializer):
    delete_image_pk_list = serializers.ListField(
        child=serializers.IntegerField()
    )
    images = serializers.ListField(
        child=serializers.ImageField()
    )

    class Meta:
        model = OrderReview
        fields = (
            'pk',
            'score',
            'comment',
            'delete_image_pk_list',
            'images',
        )

    def update(self, instance, validated_data):
        images = validated_data.pop('images', [])
        delete_image_pk_list = validated_data.pop('delete_image_pk_list')
        print('delete_image_pk_list:', delete_image_pk_list)
        with transaction.atomic():
            instance = super().update(instance, validated_data)
            # instance.images.filter(pk__in=delete_image_pk_list).delete()
            # 지우는 과정에서 파일이 삭제되도록 delete()를 직접 호출
            for image in instance.images.filter(pk__in=delete_image_pk_list):
                image.delete()

            for image in images:
                instance.images.create(image=image)
        return instance

    def to_representation(self, instance):
        return OrderReviewSerializer(instance).data
