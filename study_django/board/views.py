from django.shortcuts import render, redirect
from .models import Board
import requests as req
from django.http import JsonResponse
# Create your views here.

def gowrite(request):
    return render(request, "write.html")


def writeBoard(request): 
    if request.method == 'POST':
        if request.POST['boardTitle']:
            newBoard = Board.objects.create(
                boardTitle=request.POST['boardTitle'],
                boardContent=request.POST['boardContent'],
            )
    
    
    return redirect("/board/list")

def goList(request):
    
    allBoard = Board.objects.all()
     # 쿼리셋을 Python 객체로 변환하여 context에 추가
    board_data = [{"title": board.boardTitle, "boardContent": board.boardContent} for board in allBoard]

    # 템플릿에 객체를 넘겨주기
    return render(request, 'list.html', {'boards': board_data})