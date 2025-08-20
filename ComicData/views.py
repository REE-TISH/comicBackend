from rest_framework import generics
from .models import Comic, ComicGroup,Chapter
from .serializers import ComicSerializer, ComicGroupSerializer,ComicDetailSerializer,ChapterSerializer
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100
# For getting list of all the comics
class ComicListView(generics.ListAPIView):
    queryset = Comic.objects.all()
    serializer_class = ComicSerializer  
    pagination_class = CustomPageNumberPagination

class ComicGroupListView(generics.ListAPIView):
    queryset = ComicGroup.objects.all()
    serializer_class = ComicGroupSerializer
    pagination_class = CustomPageNumberPagination

class ComicGroupDetailView(generics.RetrieveAPIView):
    queryset = ComicGroup.objects.all()
    serializer_class = ComicGroupSerializer
    lookup_field = 'id'

class ComicDetailView(generics.RetrieveAPIView):
    queryset = Comic.objects.all()
    serializer_class = ComicDetailSerializer
    lookup_field = 'id'

class ChapterView(generics.RetrieveAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    lookup_field = 'id'

    def get_object(self,*args,**kwargs):
        comic = Comic.objects.get_object_or_404(id=self.kwargs['comic_id'])
        chapter = Chapter.objects.get_object_or_404(comic=comic,chapter_number=self.kwargs['id'])  
    
        return chapter      


