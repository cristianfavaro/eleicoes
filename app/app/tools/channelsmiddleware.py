from channels.auth import AuthMiddlewareStack
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AnonymousUser
from urllib.parse import parse_qs
from channels.db import database_sync_to_async
 

@database_sync_to_async
def get_user(scope):
    #validando se o token existe e se foi passado no url.
    token = parse_qs(scope["query_string"].decode("utf8")).get("Token") 
    
    try:
        token_obj = Token.objects.get(key=token[0])
        return token_obj.user

    except (Token.DoesNotExist, IndexError):
        return AnonymousUser()


class TokenAuthMiddleware:
    """
    Inner class that is instantiated once per scope.
    """

    def __init__(self, app):
        self.app = app
 
    async def __call__(self, scope, receive, send):
        
        scope['user'] = await get_user(scope)
        # Instantiate our inner application

        return await self.app(scope, receive, send)
                
TokenAuthMiddlewareStack = lambda inner: TokenAuthMiddleware(AuthMiddlewareStack(inner))