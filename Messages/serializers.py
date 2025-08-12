from rest_framework.serializers import ModelSerializer
from .models import ComicGroupMessage


class ComicGroupMessageSerializer(ModelSerializer):
    class Meta:
        model = ComicGroupMessage
        fields = '__all__'