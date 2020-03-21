from .models import Model
from rest_framework import serializers

class ModelSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    class Meta:
        model = Model
        fields = '__all__'