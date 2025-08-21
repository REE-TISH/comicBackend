from rest_framework import generics
from .models import ComicGroupMessage,Comments,InboxComments
from ComicData.models import ComicGroup,Chapter,Comic
from .serializers import ComicGroupMessageSerializer,CommentSectionSerializer,InboxCommentsSerializer
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


# Create your views here.
class CustomPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class ComicGroupMessageListView(generics.ListAPIView):
    queryset = ComicGroupMessage.objects.all()
    serializer_class = ComicGroupMessageSerializer
    pagination_class = CustomPageNumberPagination


    def get_queryset(self):
        comicGroup = ComicGroup.objects.get(id=self.kwargs['group_id'])
        return comicGroup.messages.all()
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        if not serializer.data:
            return Response({"detail": "No messages found for this comic group.",'status': 404})
        return Response(serializer.data)

class CommentListView(generics.ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSectionSerializer

    def get_queryset(self):
        comic = Comic.objects.get(id=self.kwargs['comic_id'])
        if not comic:
            return []
        chapter = Chapter.objects.get(chapter_number=self.kwargs['chapter_no'],comic=comic)
        if not chapter:
            return []
        return chapter.ChapterComments.all()


class CommentAddView(generics.CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSectionSerializer

    def perform_create(self, serializer):
        comic = Comic.objects.get(id=self.kwargs['comic_id'])
        chapter = Chapter.objects.get(chapter_number=self.kwargs['chapter_no'])
        serializer.save(related_chapter=chapter)


class InBoxCommentAddView(generics.CreateAPIView):
    queryset = InboxComments.objects.all()
    serializer_class = InboxCommentsSerializer

    def perform_create(self, serializer):
        ParentMsg = Comments.objects.get(id=self.kwargs['msg_id'])
        serializer.save(ParentMsg=ParentMsg)

