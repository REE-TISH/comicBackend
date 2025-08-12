from rest_framework import generics
from .models import Comic, ComicGroup
from .serializers import ComicSerializer, ComicGroupSerializer

# For getting list of all the comics
class ComicListView(generics.ListAPIView):
    queryset = Comic.objects.all()
    serializer_class = ComicSerializer  


class ComicGroupListView(generics.ListAPIView):
    queryset = ComicGroup.objects.all()
    serializer_class = ComicGroupSerializer

