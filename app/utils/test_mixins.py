from django.core.exceptions import ImproperlyConfigured
from django.urls import reverse, resolve


class ReverseResolveTestMixin(object):
    MODEL = None
    VIEW = None
    URL = None
    VIEW_NAME = None
    URL_KWARGS = {}

    def get_model(self):
        if self.MODEL is None:
            raise ImproperlyConfigured('ReverseResolveMixin require "MODEL"')
        return self.MODEL

    def get_view(self):
        if self.VIEW is None:
            raise ImproperlyConfigured('ReverseResolveMixin require "VIEW"')
        return self.VIEW

    def get_url(self):
        if self.URL is None:
            raise ImproperlyConfigured('ReverseResolveMixin require "URL"')
        return self.URL.format(**self.URL_KWARGS)

    def get_view_name(self):
        if self.VIEW_NAME is None:
            raise ImproperlyConfigured('ReverseResolveMixin require "VIEW_NAME"')
        return self.VIEW_NAME

    def test_reverse(self):
        self.assertEqual(
            reverse(self.get_view_name(), kwargs=self.URL_KWARGS),
            self.get_url()
        )

    def test_resolve(self):
        resolver_match = resolve(self.get_url())
        self.assertEqual(
            resolver_match.func.__name__,
            self.get_view().as_view().__name__)
        self.assertEqual(
            resolver_match.view_name,
            self.get_view_name())
