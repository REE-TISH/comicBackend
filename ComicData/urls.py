from django.urls import path
from . import views

urlpatterns = [ 
    path('comics/', views.ComicListView.as_view(), name='comic-list'),
    path('comic-groups/', views.ComicGroupListView.as_view(), name='comic-group-list'),
]