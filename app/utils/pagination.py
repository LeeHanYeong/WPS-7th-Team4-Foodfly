from collections import OrderedDict

from rest_framework import pagination
from rest_framework.response import Response


class CustomPageNumberPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next_page', self.page.next_page_number() if self.page.has_next() else None),
            ('previous_page', self.page.previous_page_number() if self.page.has_previous() else None),
            ('results', data)
        ]))


class Pagination10(CustomPageNumberPagination):
    page_size = 10
    max_page_size = 50
    page_size_query_param = 'page-size'


class Pagination20(CustomPageNumberPagination):
    page_size = 20
    max_page_size = 100
    page_size_query_param = 'page-size'


class Pagination30(CustomPageNumberPagination):
    page_size = 30
    max_page_size = 150
    page_size_query_param = 'page-size'


class Pagination50(pagination.PageNumberPagination):
    page_size = 50
    max_page_size = 250
    page_size_query_param = 'page-size'
