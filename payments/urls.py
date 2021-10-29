from rest_framework import routers
from django.urls import path, include
from .views import AccountViewSet, TransferViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('openaccount', AccountViewSet, basename='openaccount')
router.register('transfer', TransferViewSet, basename='transfer')

urlpatterns = [
    path('', include(router.urls))
]