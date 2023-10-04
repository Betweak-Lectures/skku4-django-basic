from django.urls import path

from . import views

urlpatterns = [
    path('', views.board_list, name='index'),
    path('comments/',
         views.comment_list,
         name="comment_list"),
]
