from rest_framework.pagination import CursorPagination, PageNumberPagination
from rest_framework.response import Response

class CustomCursorPagination(CursorPagination):
    page_size = 55
    page_size_query_param = 'page_size'
    ordering = ['-id']
    max_page_size = 100

    def get_paginated_response(self, data):

        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'results': data
        })

    def get_ordering(self, request, queryset, view):
        #Ajuste para buscar a ordem na viewset se tiver
        viewset_ordering = getattr(view, 'ordering', None)
        if viewset_ordering:
            self.ordering = viewset_ordering
        return super().get_ordering(request, queryset, view)
    

class CustomPagination(PageNumberPagination):
    page_size = 40
    page_size_query_param = 'page_size'
    max_page_size = 300

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'page_size': self.page_size,
            'results': data
        })