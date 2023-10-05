from django.http import HttpResponse
from django.shortcuts import render

from .models import Board, Comment


def index(request):
    board_list = Board.objects.prefetch_related('comment_set').all()

    return render(request, "board/index.html",
                  {'board_list': board_list})


def board_detail(request, board_id):
    board = Board.objects.get(pk=board_id)

    return render(request,
                  "board/detail.html",
                  {'board': board})


def board_write(request):
    return render(request,
                  "board/write.html",
                  {'board'})


# def index(request):
#     # return HttpResponse("Hello World, I am Younsoo!")
#     sample_list = range(10)

#     return render(request, 'board/index.html',
#                   {'name': '유저', 'sample': sample_list})


# """
# board_list라는 view 함수를 만들고 /board 로 접속하면
# 게시글에 대한 전체 게시글을 리스트 (HTML: ul, li 태그 이용)로 보여주세요.
# """


# def board_list(request):
#     qs = Board.objects.all()

#     html = ""
#     for board in qs:
#         html += f"<li><a href='/board/{board.id}'>\
#             {board.title}\
#                 </a></li>"
#     html = f"<ul>{html}</ul>"

#     return HttpResponse(html)


# """/board/comments로 접속하면 모든 댓글을 조회하도록 해주세요.
#     조회내용에 대한 형식은 다음과 같습니다.
#     (<ul>
#     <li>코멘트id | 댓글내용 | board_id </li>
#     …
#     </ul>)
# """


# def comment_list(request):
#     qs = Comment.objects.all()

#     html = ""
#     for comment in qs:
#         html += f"<li>{comment.id} | \
#             {comment.content} | {comment.board_id} </li>"
#     html = f"<ul>{html}</ul>"

#     return HttpResponse(html)


# """
# 각 게시글을 클릭 가능하게 해주시고,
# 클릭에 대한 url은 /board/<id> 로 해주세요.
# (<id>는 board에 대한 id(pk)값
# """

# # (*args, **kwargs)


# def board_detail(request, board_id):
#     qs = Board.objects.get(id=board_id)
#     comment_list = qs.comment_set.all()

#     html = f"<h1>{qs.title}</h1> \
#         <div>{qs.content}</div>"

#     html += "<ul>"
#     for comment in comment_list:
#         html += f"<li>{comment.content}</li>"
#     html += "</ul>"

#     return HttpResponse(html)
