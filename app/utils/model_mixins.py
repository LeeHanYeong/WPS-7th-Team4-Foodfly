from django.db import models

__all__ = (
    'CreatedMixin',
    'ModifiedMixin',
    'TimeStampedMixin',
)


class CreatedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class ModifiedMixin(models.Model):
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TimeStampedMixin(CreatedMixin, ModifiedMixin):
    class Meta:
        abstract = True
