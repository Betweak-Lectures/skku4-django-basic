from django.http import HttpResponse

from .models import Board, Comment


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
        html += f"<li>{board.title}</li>"
    html = f"<ul>{html}</ul>"

    return HttpResponse(html)


"""/board/comments로 접속하면 모든 댓글을 조회하도록 해주세요. 
    조회내용에 대한 형식은 다음과 같습니다.
    (<ul> 
    <li>코멘트id | 댓글내용 | board_id </li>
    …
    </ul>)
"""


def comment_list(request):
    qs = Comment.objects.all()

    html = ""
    for comment in qs:
        html += f"<li>{comment.id} | \
            {comment.content} | {comment.board_id} </li>"
    html = f"<ul>{html}</ul>"

    return HttpResponse(html)
