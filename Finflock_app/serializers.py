from rest_framework import serializers
from .models import Table1, Table2

class Table2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Table2
        fields = '__all__'

class Table1Serializer(serializers.ModelSerializer):
    table2_items = Table2Serializer(many=True, read_only=True)

    class Meta:
        model = Table1
        fields = '__all__'
