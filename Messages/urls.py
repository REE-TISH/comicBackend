from django.urls import path
from . import views

urlpatterns = [
    path('group/<str:group_id>', views.ComicGroupMessageListView.as_view(), name='comic-group-message-list'),
    path('commentList/',views.CommentListView.as_view(),name='comment-list'),
    path('addComments/',views.CommentAddView.as_view(),name='comment-add'),
]