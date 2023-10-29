
def paginate(serializer_class=None, pagination_class=None):
    def decorator(function):
        from rest_framework.response import Response
        from functools import wraps
        from django.db.models import QuerySet
    

        """
        Decorator legal que tornar o action em queryset com paginacao.
        """
        @wraps(function)
        def wrapper(self, *args, **kwargs):
            
            
            serializer = serializer_class if serializer_class else self.get_serializer_class()
            
            if pagination_class:
                self.pagination_class = pagination_class

            queryset = function(self, *args, **kwargs)
            assert isinstance(queryset, (list, QuerySet)), "apply_pagination expects a List or a QuerySet"


            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = serializer(queryset, many=True)
            
            return Response(serializer.data)
        return wrapper
    return decorator
