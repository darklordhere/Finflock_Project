from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Table1ViewSet, Table2ViewSet

router = DefaultRouter()
router.register(r'table1', Table1ViewSet)
router.register(r'table2', Table2ViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
