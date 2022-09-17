from dataclasses import fields
from rest_framework import serializers
from project.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'