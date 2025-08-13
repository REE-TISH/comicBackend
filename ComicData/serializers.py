from rest_framework import serializers
from .models import Comic,ComicGroup,Chapter

class ComicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comic
        fields = '__all__'

class ComicDetailSerializer(serializers.ModelSerializer):
    chapters = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Comic
        fields = ['id','title','author','description','published_date','cover_image','rating','genre','chapters']

    def get_chapters(self,obj):
        chapters = len(obj.chapters.all())
        return chapters

class ComicGroupSerializer(serializers.ModelSerializer):
    lastMessage = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ComicGroup
        fields = ['id','name' , 'avatar','lastMessage']

    def get_lastMessage(self, obj):
        last_message = obj.messages.all().last() if obj.messages.exists() else None
        if last_message:
            return last_message.body
               
            
        return None
    
class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter   
        fields = '__all__'