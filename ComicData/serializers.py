from rest_framework import serializers
from .models import Comic,ComicGroup,Chapter,Novels,NovelChapter


# Comic Serializer to send Comic Data
class ComicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comic
        fields = '__all__'


# Serialize Detailed Extra data when user is on Novel detail page
class ComicDetailSerializer(serializers.ModelSerializer):
    chapters = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Comic
        fields = ['id','title','author','description','published_date','cover_image','rating','genre','chapters']

    def get_chapters(self,obj):
        chapters = len(obj.chapters.all())
        return chapters

# Comic Groups serializer
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

# Comic Chapter serializers
class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter   
        fields = '__all__'

# Novel data Serializer
class NovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Novels
        fields = '__all__'

# Novel Chapter data Serializer
class NovelChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NovelChapter
        fields = '__all__'

# Novel Detail Page data serializer
class NovelDetailSerializer(serializers.ModelSerializer):
    chapters = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Novels
        fields = ['id','title','author','description','published_date','cover_image','rating','genre','chapters']

    def get_chapters(self,obj):
        chapters = len(obj.novelChapters.all())
        return chapters