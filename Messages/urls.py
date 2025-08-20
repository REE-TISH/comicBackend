from django.urls import path
from . import views

urlpatterns = [
    path('group/<str:group_id>', views.ComicGroupMessageListView.as_view(), name='comic-group-message-list'),
    path('commentList/<str:chapter_id>/',views.CommentListView.as_view(),name='comment-list'),
    path('addComments/<str:chapter_id>/',views.CommentAddView.as_view(),name='comment-add'),
    path('addInBoxComment/<str:msg_id>/',views.InBoxCommentAddView.as_view(),name='Inbox-comment'),
]
