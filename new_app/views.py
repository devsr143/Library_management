from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from new_app.models import Library
from new_app.serializer import LibrarySerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = LibrarySerializer
    queryset = Library.objects.all()
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Category','Is_available']