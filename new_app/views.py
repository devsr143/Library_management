from rest_framework import viewsets

from new_app.models import Library
from new_app.serializer import LibrarySerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = LibrarySerializer
    queryset = Library.objects.all()
