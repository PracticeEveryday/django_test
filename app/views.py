from django.http import HttpRequest, HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import render
from app.serializers import BoardSerializer

from .models import Board
from .permissions import UpdateOwnProfile


def index(request: HttpRequest) -> HttpResponse:
    # return HttpResponse('hello')
    qs = Board.objects.all()
    # qs = [
    #     {"id": 1, "title": "post#1"},
    #     {"id": 2, "title": "post#2"}
    # ]
    return render(request, "app/index.html", {
        # post_list라는 이름으로 템플릿에서 참조 가능하다!!!
        "post_list": qs
    })


class BoardViewSet(ModelViewSet):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, UpdateOwnProfile, )

