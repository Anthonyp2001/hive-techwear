from django.conf import settings
from rest_framework .response import responses
from rest_framework.response import Response
from rest_framework import pagination

class customizePagination(pagination.Pagenumberpagniation):
    
    def get_paginated_response(self, data):
        if not data:
            total_pages = 0
        else:
            total_pages = self.page.paginator.num_pages


        return Response ({
            'count': self.page.paginator.count,
            'total_pages': total_pages,
            'current': self.page.number,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })