from django.urls import path, include
from rest_framework.routers import DefaultRouter

from new_app.views import UserViewSet

router = DefaultRouter()
router.register('Library',UserViewSet,basename='Library')
urlpatterns = [
    path('',include(router.urls)),
]