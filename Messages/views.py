from rest_framework import generics
from .models import ComicGroupMessage
from ComicData.models import ComicGroup
from .serializers import ComicGroupMessageSerializer
from rest_framework.response import Response

# Create your views here.
class ComicGroupMessageListView(generics.ListAPIView):
    queryset = ComicGroupMessage.objects.all()
    serializer_class = ComicGroupMessageSerializer


    def get_queryset(self):
        comicGroup = ComicGroup.objects.get(id=self.kwargs['group_id'])
        return comicGroup.messages.all()
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        if not serializer.data:
            return Response({"detail": "No messages found for this comic group.",'status': 404})
        return Response(serializer.data)
