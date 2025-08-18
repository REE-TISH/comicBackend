from rest_framework.serializers import ModelSerializer
from .models import ComicGroupMessage,Comments


class ComicGroupMessageSerializer(ModelSerializer):
    class Meta:
        model = ComicGroupMessage
        fields = '__all__'

class CommentSectionSerializer(ModelSerializer):
    class Meta:
        model = Comments
        field = '__all__'