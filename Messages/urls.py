from django.urls import path
from . import views

urlpatterns = [
    path('group/<str:group_id>', views.ComicGroupMessageListView.as_view(), name='comic-group-message-list'),
]