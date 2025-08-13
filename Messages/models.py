from django.db import models
from ComicData.models import ComicGroup

# Create your models here.
class ComicGroupMessage(models.Model):
    comic_group = models.ForeignKey(ComicGroup, on_delete=models.CASCADE, related_name='messages')
    sender = models.CharField(max_length=100)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    avatar = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.sender} in {self.comic_group.name}: {self.body[:30]}..."
