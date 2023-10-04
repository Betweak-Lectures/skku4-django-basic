from django.http import HttpResponse

from .models import Board


def index(request):
    return HttpResponse("Hello World, I am Younsoo!")


"""
board_list라는 view 함수를 만들고 /board 로 접속하면 
게시글에 대한 전체 게시글을 리스트 (HTML: ul, li 태그 이용)로 보여주세요. 
"""


def board_list(request):
    qs = Board.objects.all()

    html = ""
    for board in qs:
        html += "<li>{board.title}</li>"
    html = f"<ul>{html}</ul>"

    return HttpResponse(html)
