from django.db import transaction
from rest_framework import serializers

from ..models import OrderReview, OrderReviewImage

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
            'user',
            'score',
            'comment',
            'images',
        )

    def create(self, validated_data):
        images = validated_data.pop('images')
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
        with transaction.atomic():
            instance = super().update(instance, validated_data)
            instance.images.filter(pk__in=delete_image_pk_list).delete()
            for image in images:
                instance.images.create(image=image)
        return instance

    def to_representation(self, instance):
        return OrderReviewSerializer(instance).data
