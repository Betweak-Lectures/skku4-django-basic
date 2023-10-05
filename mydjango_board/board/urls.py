from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:board_id>', views.board_detail, name="detail"),

    #     path('', views.board_list, name='index'),
    #     path('<int:board_id>/',
    #          views.board_detail,
    #          name="board_detail"),
    #     path('comments/',
    #          views.comment_list,
    #          name="comment_list"),
]
