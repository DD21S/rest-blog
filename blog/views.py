from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework import permissions

from .serializers import PostSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly
from .models import Post

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    '''
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    This viewset automatically provides `list` and `retrieve` actions.
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer