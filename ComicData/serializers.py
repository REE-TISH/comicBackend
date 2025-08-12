from rest_framework.serializers import ModelSerializer
from .models import Comic,ComicGroup

class ComicSerializer(ModelSerializer):
    class Meta:
        model = Comic
        fields = '__all__'

class ComicGroupSerializer(ModelSerializer):
    class Meta:
        model = ComicGroup
        fields = '__all__'