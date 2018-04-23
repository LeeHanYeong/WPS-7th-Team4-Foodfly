from django.conf import settings
from django.db import models

from utils.model_mixins import CreatedMixin
from .order import Order

__all__ = (
    'OrderReview',
    'OrderReviewImage',
)


class OrderReviewManager(models.Manager):
    def create_mock(self, user, order, images=None):
        review = self.create(
            user=user,
            order=order,
            score=1,
            comment='Mock comment'
        )
        if images:
            for image in images:
                OrderReviewImage.objects.create_mock(
                    review=review,
                    image=image
                )
        return review


class OrderReview(CreatedMixin, models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='reviews',
        blank=True,
        null=True,
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    score = models.PositiveSmallIntegerField(default=5)
    comment = models.TextField()

    objects = OrderReviewManager()


class OrderReviewImageManager(models.Manager):
    def create_mock(self, review, image):
        review_image = self.create(
            review=review,
        )
        review_image.image.save('mock.jpg', image)
        return review_image


class OrderReviewImage(CreatedMixin, models.Model):
    review = models.ForeignKey(OrderReview, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='review')

    objects = OrderReviewImageManager()
