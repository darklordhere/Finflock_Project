from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Table1, Table2
from .serializers import Table1Serializer, Table2Serializer

class Table1ViewSet(viewsets.ModelViewSet):
    queryset = Table1.objects.all()
    serializer_class = Table1Serializer

    # Enable filtering and ordering
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['name', 'date']
    ordering_fields = '__all__'
    ordering = ['name']

class Table2ViewSet(viewsets.ModelViewSet):
    queryset = Table2.objects.all()
    serializer_class = Table2Serializer

    # Enable filtering and ordering
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = '__all__'
    ordering = ['description']
